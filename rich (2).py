from rich.console import Console
from rich.text import Text

console = Console()
title=Text("🥰 Selamlar Dostlar", style="bold magenta")

description= Text()
description.append("Çok ",style="bold")
description.append("Güzelsin ",style="bold red")


highlight=Text("Bu Hafta Yapman Gerekenler", style="underline blue")
highlight.append("\n⚽ Futbol Oynamak", style="bold green")
highlight.append("\n🥊 Dövüşe gitmek", style="bold yellow")
highlight.append("\n🤿 Yüzmeye gitmek", style="bold red")

console.print(title)
console.print(description)
console.print(highlight)