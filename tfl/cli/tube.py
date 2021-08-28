from typing import List

import typer
from rich.console import Console
from rich.style import Style
from rich.theme import Theme

from tfl.api.line import by_mode
from tfl.api.presentation.entities.line import LineStatus

app = typer.Typer()

BASE_STYLE = Style(bold=True, bgcolor="white", italic=True)
line_styles = {
    "central": Style(color="#E32017"),
    "bakerloo": Style(color="#B36305"),
    "circle": Style(color="#FFD300", bgcolor="black"),
}
line_styles = {k: BASE_STYLE + v for k, v in line_styles.items()}

status_severity_style = {"good_service": Style(color="green")}


def summarise_statuses(statuses: List[LineStatus]) -> str:
    agg = []
    for status in statuses:
        if status.statusSeverity == 10:
            agg.append("[good_service]Good service[/good_service]")
    return "".join(agg)


console = Console(theme=Theme({**line_styles, **status_severity_style}))


@app.command()
def status() -> None:
    lines = by_mode("tube", status=True)
    for line in lines:
        console.print(f" [{line.id}]{line.name}[/{line.id}] " + summarise_statuses(line.lineStatuses))
