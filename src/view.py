from dash.html import (Div, Video)
import dash_mantine_components as dmc
from dash.dcc import (Markdown, Interval)


class View:


    def __init__(self, items):
        """  """

        self.items = items
        self._uploadRateSeconds = 40


    def _buildItem(
            
        self,
        width = 1, 
        style = {},
        height = 1,
        corpus = None,
        visible = True,
        background = None,
        contentType = "markdown",

    ):
        """  """

        return Div(

            className = "gridItem",
            children = {

                "video" : self._buildItemVideo,
                "markdown" : self._buildItemMarkdown,
                "my-projects" : self._buildItemProjects,
                "my-tech-stack" : self._buildItemTechStack

            }[contentType](corpus) if corpus else None,
            style = {

                **style,
                "gridRow" : f"span {height}",
                "gridColumn" : f"span {width}",
                "backgroundImage" : f"url({background})",
                "visibility" : "visible" if visible else "hidden"

            }
            
        )


    def _buildItemMarkdown(self, markdown):
        """  """

        return Markdown(

            className = "markdownExtended",
            children = "\n".join([
                
                {

                    str: m,
                    list: " ".join(m) + "\n"

                }[type(m)]
                
            for m in markdown])

        )


    def _buildItemVideo(self, video):
        """  """

        return Video(

            src = video,
            loop = False,
            muted = True,
            className = "videoExtended",
            id = {"type" : "video", "index" : video}

        )


    def _buildItemProjects(self, projects):
        """  """

        pass


    def _buildItemTechStack(self, techStack):
        """  """

        pass


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