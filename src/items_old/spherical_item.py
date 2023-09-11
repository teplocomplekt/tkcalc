
import math
from items_old.base_item import BaseItem, my_logger
from items_old.base_thorspherical_item import BaseThorSphericalItem
from render_old.drawer import CENTER_POINT, LineWidth, Color


class SphericalItem(BaseThorSphericalItem):

    @property
    def _title_template(self):
        return [
            self._id,
            self.R,
            self.s]

    @property
    def _angle(self):
        return math.acos(self._id / 2 / self.R)

    @property
    def _angle1(self):
        return math.asin(self.d / 2 / self.R)

    @property
    def _height_R(self):
        return math.tan(self._angle) * (self._id / 2)

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
        c3 = self.s * 0.1
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
        L1 = (-(self._id) / self.scale / 2, 0)
        R1 = (self._id / self.scale / 2, 0)
        L2 = (-(self.R + self.s) * math.cos(self._angle) / self.scale, (self._height_R - (self.R + self.s) * math.sin(self._angle)) / self.scale)
        R2 = ((self.R + self.s) * math.cos(self._angle) / self.scale, (self._height_R - (self.R + self.s) * math.sin(self._angle)) / self.scale)
        L3 = (-(self.d) / 2 / self.scale, self._height / self.scale)
        R3 = (self.d / 2 / self.scale, self._height / self.scale)
        L4 = (-(self.d) / 2 / self.scale, (self._height - self.s) / self.scale)
        R4 = (self.d / 2 / self.scale, (self._height - self.s) / self.scale)
        H0 = (R1[0], R4[1])
        A0 = (0, self._height_R / self.scale)
        drawer.poly_line([
            (0, 0),
            L1,
            L2])

        # Рисуем левую половинку, внешнюю часть
        drawer.arc(*A0, (self.R + self.s) / self.scale, math.pi + self._angle, - math.pi / 2 - self._angle1)
        drawer.stroke()
        # Рисуем левую половинку, внутреннюю часть
        drawer.arc(*A0, self.R / self.scale, math.pi + self._angle, -math.pi / 2 - self._angle1)
        drawer.stroke()

        # Рисуем правую половинку
        drawer.poly_line([(0, 0), R1, R2])
        # Рисуем правую половинку, внешнюю часть
        drawer.arc_negative(*A0, (self.R + self.s) / self.scale, -self._angle, -math.pi / 2 + self._angle1)
        drawer.stroke()
        # Рисуем правую половинку, внутреннюю часть
        drawer.arc_negative(*A0, self.R / self.scale, -self._angle, -math.pi / 2 + self._angle1)
        drawer.stroke()

        # Рисуем тех отверстие
        if self.d > 0:
            drawer.line(L3, R3)
            drawer.line(R3, R4)
            drawer.line(R4, L4)
            drawer.line(L4, L3)
            drawer.stroke()

        # Размер D
        drawer.dimension(L2, R2, f'⌀{self.D}±2', 10)  # ⌀
        # drawer.dimension_diameter(L1, R1, f'{self.D}±2', 10)  # ⌀

        # Размер s
        drawer.dimension_thickness(
            center=A0,
            radius=self.R / self.scale,
            thickness=self.s / self.scale,
            text=f'{self.s}*',
            angle=((math.pi / 2 - self._angle - self._angle1) * 2 / 3 + self._angle),
            offset=5
        )

        # Размер d
        if self.d > 0:
            drawer.dimension(L4, R4, f'⌀{self.d}*', -10, 'right', 'out')
            # drawer.dimension_diameter(L4, R4, f'{self.d}*', -10, 'right', 'out')

        # Размер H
        H = int(round(self.get_total_height))
        drawer.set_line_style(LineWidth.THIN, Color.BLACK)
        drawer.line(R4, H0)
        drawer.stroke()
        drawer.dimension(H0, R1, f'{H}±10', -10, 'center', 'in')

        # Размер R
        drawer.radius_dimension(
            center=A0,
            radius=self.R / self.scale,
            text=f'R{self.R}',
            # angle=(self._angle / 3 + math.pi / 4 - self._angle1),
            angle=((math.pi / 2 - self._angle - self._angle1) * 1 / 3 + self._angle),
            offset=5
        )

        # смещаем начало координат обратно в левый нижний угол листа
        drawer.context.restore()

    
    def check_s(self):
        if self.s < self.s or self.s < 40:
            return True
        my_logger.info('Ошибка в s.(3 < s < 40)')
        return False

    
    def check_values(self):
        """
        if (name_bottum == "Сферическое")
        {
            bool b_value[3]={true, true, true};
            // check D
            if ((id>=300)&&(id<=4000)){b_value[0] = true;}else {b_value[0] = false; ShowMessage("Ошибка в D.(300 < D < 4000)" );}
            // check R
            if ((R>=id*0.75)&&(R<10000)){b_value[1] = true;}else {b_value[1] = false; ShowMessage("Ошибка в R.(D*0.75 < R < 10000)" );}
            // check s
            if (3 < s && s < 40) {b_value[2] = true;}else {b_value[2] = false; ShowMessage("Ошибка в s.(3 < s < 40)" );}
            bool_value = b_value[0] & b_value[1] & b_value[2];
        }
        """

        b_value = {
            'D': self.check_D(),
            'Dm': True,
            'R': self.check_R(),
            'r': True,
            's': self.check_s(),
            'h': True }
        return b_value
