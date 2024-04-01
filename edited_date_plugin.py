import datetime
from mkdocs.plugins import BasePlugin

class EditedDatePlugin(BasePlugin):
    def on_page_markdown(self, markdown, page, **kwargs):
        edited_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"<!-- Edited: {edited_date} -->\n\n{markdown}"
