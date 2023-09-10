import math
from items_old.base_item import BaseItem, my_logger
from items_old.base_thorspherical_item import BaseThorSphericalItem
from render.drawer import CENTER_POINT, LineWidth, Color


class FlatItem(BaseThorSphericalItem):

    def __init__(self=None, **args):
        super().__init__(**args)
        # self.R = 10000000

    @property
    def _title_template(self):
        return [
            self._id,
            self.r,
            self.h,
            self.s]

    @property
    def _get_K(self):
        K = 0.35
        return K

    @property
    def _get_Ko(self):
        Ko = 1
        return Ko

    @property
    def _get_Dr(self):
        return self._id - self.r * 2

    @property
    def get_k(self):
        sp = self.p * self._id / (2 * self._get_Q * self._get_f - self.p)
        k = self.s / (sp + self._get_c)
        return k

    @property
    def get_k1(self):
        s1p = self._get_K * self._get_Ko * self._get_Dr * pow(self.p / self._get_f * self._get_Q, 0.5)
        k1 = self.s / (s1p + self._get_c)
        return k1

    @property
    def get_total_pressure(self):
        if self.r <= self.r or self.r <= min(self.s, 0.1 * self._id):
            my_logger.info('Формула расчета давления не применима max(s;0.25 * s1) ≤ r ≤ min(s1;0.1 * D)')

        pressure = pow((self.s - self._get_c) / self._get_K * self._get_Ko * self._get_Dr,
                       2) * self._get_Q * self._get_f
        return pressure

    def draw(self, drawer):
        drawer.context.save()
        drawer.context.translate(CENTER_POINT[0], CENTER_POINT[1] + self.get_total_height / 2 / self.scale)
        drawer.set_line_style(LineWidth.MEDIUM, Color.BLACK)
        L1 = (-self._id / self.scale / 2, self.h / self.scale)
        R1 = (self._id / self.scale / 2, self.h / self.scale)
        L2 = ((-self._id / 2 - self.s) / self.scale, self.h / self.scale)
        R2 = ((self._id / 2 + self.s) / self.scale, self.h / self.scale)
        L3 = (-self._id / self.scale / 2, 0)
        R3 = (self._id / self.scale / 2, 0)
        L4 = ((-self._id / 2 - self.s) / self.scale, 0)
        R4 = ((self._id / 2 + self.s) / self.scale, 0)
        L5 = ((-self._id / 2 + self.r) / self.scale, -self.r / self.scale)
        R5 = ((self._id / 2 - self.r) / self.scale, -self.r / self.scale)
        L6 = ((-self._id / 2 + self.r) / self.scale, (-self.r - self.s) / self.scale)
        R6 = ((self._id / 2 - self.r) / self.scale, (-self.r - self.s) / self.scale)
        L7 = (-self.d / 2 / self.scale, -self.r / self.scale)
        R7 = (self.d / 2 / self.scale, -self.r / self.scale)
        L8 = (-self.d / 2 / self.scale, (-self.r - self.s) / self.scale)
        R8 = (self.d / 2 / self.scale, (-self.r - self.s) / self.scale)
        AL = ((-self._id / 2 + self.r) / self.scale, 0)
        AR = ((self._id / 2 - self.r) / self.scale, 0)
        H0 = (R2[0], R8[1])

        drawer.poly_line([
            (0, self.h / self.scale),
            L1,
            L3])

        # Рисуем левую половинку
        drawer.poly_line([(0, self.h / self.scale), L1, L3])
        drawer.arc(*AL, self.r / self.scale, math.pi, 3 / 2 * math.pi)
        drawer.line(L5, L7)
        drawer.stroke()

        # # Рисуем левую половинку, внутреннюю часть
        drawer.poly_line([L1, L2, L4])
        drawer.arc(*AL, (self.r + self.s) / self.scale, math.pi, 3 / 2 * math.pi)
        drawer.line(L6, L8)
        drawer.stroke()

        # # Рисуем правую половинку
        drawer.poly_line([(0, self.h / self.scale), R1, R3])
        drawer.arc_negative(*AR, self.r / self.scale, 0, -math.pi / 2)
        drawer.line(R5, R7)
        drawer.stroke()

        # # Рисуем правую половинку, внутреннюю часть
        drawer.poly_line([R1, R2, R4])
        drawer.arc_negative(*AR, (self.r + self.s) / self.scale, 0, -math.pi / 2)
        drawer.line(R6, R8)
        drawer.stroke()

        # Рисуем тех отверстие
        if self.d > 0:
            drawer.line(L7, R7)
            drawer.line(R7, R8)
            drawer.line(R8, L8)
            drawer.line(L8, L7)
            drawer.stroke()

        # Размер D
        drawer.dimension(L2, R2, f'⌀{self.D}±2', 10)  # ⌀
        # drawer.dimension_diameter(L1, R1, f'{self.D}±2', 10)  # ⌀

        # Размер s
        drawer.dimension(R1, R2, f'{self.s}', 5, 'right', 'out')

        # Размер h
        if self.h > 0:
            drawer.dimension(L4, L2, f'{self.h}*', 5, 'right', 'out')

        # Размер d
        if self.d > 0:
            drawer.dimension(L8, R8, f'⌀{self.d}*', -10, 'right', 'out')
            # drawer.dimension_diameter(L8, R8, f'{self.d}*', -10, 'right', 'out')

        # Размер H
        h = int(round(self.get_total_height))
        drawer.set_line_style(LineWidth.THIN, Color.BLACK)
        drawer.line(R6, H0)
        drawer.stroke()
        drawer.dimension(H0, R2, f'{h}±10', -10, 'left', 'out')

        # Размер r
        if self.r > 0:
            drawer.radius_dimension(AL, self.r / self.scale, f'r{self.r}', math.pi / 4, offset=5)

        # смещаем начало координат обратно в левый нижний угол листа
        drawer.context.restore()

    def check_values(self):
        """
        if (name_bottum == "Плоское"){
            bool b_value[4]={true, true, true, true};
            // check D
            if ((id>=300)&&(id<=4000)){b_value[0] = true;}else {b_value[0] = false;ShowMessage("Ошибка в D.(300 < D < 4000)" );}
            // check r
            if (r>=30){b_value[1] = true;}else {b_value[1] = false; ShowMessage("Ошибка в r.(r >= 30)" );}
            // check s
            float min = StrToInt(data_from_db_1("0", "r_" + IntToStr(r_optimal(r)), "Check_min_s", "Diametr", FloatToStr(id))) / coef;
            float max = StrToInt(data_from_db_1("0", "r_" + IntToStr(r_optimal(r)), "Check_max_s", "Diametr", FloatToStr(id))) / coef;
            if (min < s && s < max) {b_value[2] = true;}
              else {b_value[2] = false; ShowMessage("Ошибка в s.(s > " + FloatToStr(min) + " и s < " + FloatToStr(max) + ")" );}
            //check h
            if (h>=(s * 3) && h<=(s * 5)){b_value[3] = true;}else {b_value[3] = false; ShowMessage("Ошибка в h.(h > s*3 и h < s*5)" );}
            bool_value = b_value[0] & b_value[1] & b_value[2] & b_value[3];
        }
        """

        return {
            'D': self.check_D(),
            'Dm': True,
            'R': True,
            'r': self.check_r(),
            's': self.check_s(),
            'h': self.check_h()}
