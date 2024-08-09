
# pylint: disable=all
from cg.cg import Texture,TexturePolygon,Screen


class imagem:
    def __init__(self, windows, viewports, nome_img) -> None:
        self.texture = Texture.import_texture(nome_img)
        # Obtendo a largura e altura da tela a partir do viewport
        screen_width = viewports[0][2]
        screen_height = viewports[0][3]

        # Definindo o TexturePolygon para preencher a tela
        self.polygon = TexturePolygon(
            [
                [0, 0, 0, 0],          # Canto superior esquerdo
                [0, screen_height, 0, 1],  # Canto inferior esquerdo
                [screen_width, screen_height, 1, 1], # Canto inferior direito
                [screen_width, 0, 1, 0]   # Canto superior direito
            ]
        )
        self.windows = windows
        self.viewports = viewports

    def draw(self, screen) -> None:
        pol = Screen.mapping_window(self.polygon, self.windows[0], self.viewports[0])
        Texture.scanline_with_texture(screen, pol, self.texture)