
import math
from items_old.base_item import BaseItem, my_logger
from items_old.base_thorspherical_item import BaseThorSphericalItem
from render_old.drawer import CENTER_POINT, LineWidth, Color
from utils.settings import S_MIN, S_MAX


class ThorSphericalItem(BaseThorSphericalItem):

    @property
    def _title_template(self):
        return [
            self._id,
            self.R,
            self.r,
            self.h,
            self.s]

    @property
    def _angle(self):
        return math.acos((self.D / 2 - self.r - self.s) / (self.R - self.r))

    @property
    def _angle1(self):
        return math.asin(self.d / 2 / self.R)

    @property
    def _height_R(self):
        return math.tan(self._angle) * (self.D / 2 - self.r - self.s)

    @property
    def _height1(self):
        return math.tan(math.pi / 2 - self._angle1) * self.d / 2

    @property
    def _height(self):
        return self._height_R - math.cos(self._angle1) * self.R

    @property
    def _get_c(self):
        c1 = self.c1
        c2 = self.c2
        c3 = self.s * 0.15
        c = c1 + c2 + c3
        return c

    @property
    def get_total_pressure(self):
        pressure = 2 * (self.s - self._get_c) * self._get_f * self._get_Q / (self._get_R + 0.5 * (self.s - self._get_c))
        return pressure

    def draw(self, drawer):
        drawer.context.save()
        drawer.context.translate(CENTER_POINT[0], CENTER_POINT[1] + self.get_total_height / 2 / self.scale)
        drawer.set_line_style(LineWidth.MEDIUM, Color.BLACK)
        L1 = ((-self.D / 2 + self.s) / self.scale, self.h / self.scale)
        R1 = ((self.D / 2 - self.s) / self.scale, self.h / self.scale)
        L2 = (-self.D / self.scale / 2, self.h / self.scale)
        R2 = (self.D / self.scale / 2, self.h / self.scale)
        L3 = ((-self.D / 2 + self.s) / self.scale, 0)
        R3 = ((self.D / 2 - self.s) / self.scale, 0)
        L4 = (-self.D / self.scale / 2, 0)
        R4 = (self.D / self.scale / 2, 0)
        L5 = (-self.d / 2 / self.scale, self._height / self.scale)
        R5 = (self.d / 2 / self.scale, self._height / self.scale)
        L6 = (-self.d / 2 / self.scale, (self._height - self.s) / self.scale)
        R6 = (self.d / 2 / self.scale, (self._height - self.s) / self.scale)
        AL = ((-self.D / 2 + self.r + self.s) / self.scale, 0)
        AR = ((self.D / 2 - self.r - self.s) / self.scale, 0)
        A0 = (0, self._height_R / self.scale)
        H0 = (R2[0], R6[1])
        drawer.poly_line([
            (0, self.h / self.scale),
            L1,
            L3])

        drawer.arc(*AL, self.r / self.scale, math.pi, math.pi + self._angle)
        drawer.arc(*A0, self.R / self.scale, math.pi + self._angle, -math.pi / 2 - self._angle1)
        drawer.stroke()

        # Рисуем левую половинку, внутреннюю часть
        drawer.poly_line([L1, L2, L4])
        drawer.arc(*AL, (self.r + self.s) / self.scale, math.pi, math.pi + self._angle)
        drawer.arc(*A0, (self.R + self.s) / self.scale, math.pi + self._angle, - math.pi / 2 - self._angle1)
        drawer.stroke()

        # Рисуем правую половинку
        drawer.poly_line([(0, self.h / self.scale), R1, R3])
        drawer.arc_negative(*AR, self.r / self.scale, 0, -self._angle)
        drawer.arc_negative(*A0, self.R / self.scale, -self._angle, -math.pi / 2 + self._angle1)
        drawer.stroke()

        # Рисуем правую половинку, внутреннюю часть
        drawer.poly_line([R1, R2, R4])
        drawer.arc_negative(*AR, (self.r + self.s) / self.scale, 0, -self._angle)
        drawer.arc_negative(*A0, (self.R + self.s) / self.scale, -self._angle, -math.pi / 2 + self._angle1)
        drawer.stroke()

        # Рисуем тех отверстие
        if self.d > 0:
            drawer.line(L5, R5)
            drawer.line(R5, R6)
            drawer.line(R6, L6)
            drawer.line(L6, L5)
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
            drawer.dimension(L6, R6, f'⌀{self.d}*', -10, 'right', 'out')
            # drawer.dimension_diameter(L6, R6, f'{self.d}*', -10, 'right', 'out')

        # Размер H
        H = int(round(self.get_total_height))
        drawer.set_line_style(LineWidth.THIN, Color.BLACK)
        drawer.line(R6, H0)
        drawer.stroke()
        drawer.dimension(H0, R2, f'{H}±10', -10, 'center', 'in')

        # Размер r
        if self.r > 0:
            drawer.radius_dimension(AL, self.r / self.scale, f'r{self.r}', self._angle / 2, offset=5)

        # Размер R
        drawer.radius_dimension(
            A0,
            self.R / self.scale,
            f'R{self.R}',
            angle=(self._angle / 2 + math.pi / 4 - self._angle1),
            offset=5
        )

        # смещаем начало координат обратно в левый нижний угол листа
        drawer.context.restore()


    def check_values(self):
        """
        bool Check_values(String name_bottum)
        {
          bool bool_value;float coef;
          if (density < 0.00000833) {coef = 1.2;} else coef = 1.5;
          if (name_bottum == "Торосферические") {
             bool b_value[5]={true, true, true, true, true};
               // check D
               if ((id>=300)&&(id<=4000)){ b_value[1] = true;}else {b_value[1] = false;ShowMessage("Ошибка в D.(300 < D < 4000)" );}
               // check R
               if ((R>=id*0.75)&&(R<10000)){b_value[2] = true;}else {b_value[2] = false;ShowMessage("Ошибка в R.(D*0.75 < R < 10000)" );}
               // check r
               if (r>=30){b_value[3] = true;}else b_value[3] = false;
               // check s
               String st = data_from_db_1("0", "r_150", "Check_min_s", "Diametr", FloatToStr(id));
               float min = StrToInt(data_from_db_1("0", "r_" + IntToStr(r_optimal(r)), "Check_min_s", "Diametr", FloatToStr(id))) / coef;
               float max = StrToInt(data_from_db_1("0", "r_" + IntToStr(r_optimal(r)), "Check_max_s", "Diametr", FloatToStr(id))) / coef;
               if (min < s && s < max) {b_value[4] = true;}
                  else {b_value[4] = false; ShowMessage("Ошибка в s.(s > " + FloatToStr(min) + " и s < " + FloatToStr(max) + ")" );}
               //check h
               if (h>=(s * 3) && h<=(s * 5)){b_value[0] = true;}else {b_value[0] = false;ShowMessage("Ошибка в h.(h > s*3 и h < s*5)" );}
               bool_value = b_value[0] & b_value[1] & b_value[2] & b_value[3] & b_value[4];
          }
        }
        """
        return {
            'D': self.check_D(),
            'Dm': True,
            'R': self.check_R(),
            'r': self.check_r(),
            's': self.check_s(),
            'h': self.check_h()
        }


