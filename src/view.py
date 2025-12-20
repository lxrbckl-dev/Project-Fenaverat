from dash.html import (Div, Video)
import dash_mantine_components as dmc
from dash.dcc import (Markdown, Interval)


class View:


    def __init__(self, items):
        """  """

        self.items = items
        self._uploadRateSeconds = 60


    def _buildItem(
            
            self,
            row = 1, 
            col = 1,
            style = {},
            corpus = [],
            video = None,
            header = False,
            visible = True,
            justify = None,
            background = None,
            align = "center-top"

        ):
        """  """

        return Div(

            className = "gridItem",
            children = Video(

                src = video,
                loop = False,
                muted = True,
                className = "videoExtended",
                id = {"type" : "video", "index" : video}

            ) if video else Markdown(

                className = "markdownExtended" if corpus else None,
                children = "\n".join([
                    
                    {

                        str: c,
                        list: " ".join(c) + "\n"

                    }[type(c)]

                for c in corpus]),
                style = {

                    "justifyContent" : justify,
                    "width" : "auto" if header else "100%"

                }

            ),
            style = {

                **style,
                "alignItems" : align,
                "gridRow" : f"span {row}",
                "gridColumn" : f"span {col}",
                "backgroundImage" : f"url({background})",
                "visibility" : "visible" if visible else "hidden"

            }

        )


    @property
    def build(self):
        """  """

        return dmc.MantineProvider(children = dmc.Center(children = [

            Interval(

                n_intervals = 0,
                id = "intervalId",
                interval = (1000 * self._uploadRateSeconds)

            ),
            Div(

                className = "gridContainer",
                children = [self._buildItem(**i) for i in self.items]

            )

        ]))