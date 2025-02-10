from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
import time
import re

console = Console()

def main_menu(target, recon_mode, selected_modules):
    console.clear()

    # Prepare persistent user settings panel
    target_display = target if target else "[red]No target set[/red]"
    mode_display = recon_mode if recon_mode else "[red]No mode selected[/red]"
    modules_display = ", ".join(selected_modules) if selected_modules else "[red]No modules selected[/red]"
    
    user_settings = Panel(
        f"[bold cyan]Target:[/bold cyan] [green]{target_display}[/green]\n"
        f"[bold cyan]Selected Modules:[/bold cyan] [green]{modules_display}[/green]\n"
        f"[bold cyan]Recon Mode:[/bold cyan] [green]{mode_display}[/green]\n",
        title="[bold green]User Settings[/bold green]",
        border_style="cyan",
        box=box.ROUNDED
    )
    
    console.print("[bold blue]Automated Recon Bot[/bold blue] - Interactive Menu\n")
    table = Table(title="Main Menu")
    table.add_column("Option", style="cyan")
    table.add_column("Description", style="magenta")

    table.add_row("1", "Set Target")
    table.add_row("2", "Select Recon Modules")
    table.add_row("3", "Choose Recon Mode")
    table.add_row("4", "Execute Recon")
    table.add_row("5", "View Reports")
    table.add_row("0", "Exit")

    console.print(table)
    console.print(user_settings)
    
    choice = console.input("\n[bold green]Enter your choice:[/bold green] ")
    return choice

def set_target():
    console.print("\n[bold green]Enter target domain or IP (e.g., example.com or 192.168.1.1):[/bold green]")
    target = console.input("> ").strip()

    if validate_target(target):
        target_visual = Panel(
            f"[bold cyan]Target set to:[/bold cyan] [yellow]{target}[/yellow]", 
            title="[bold green]Success[/bold green]", 
            border_style="green",
            box=box.ROUNDED
        )
        console.print(target_visual)
        return target
    else:
        console.print("[red]Invalid target! Please enter a valid domain or IP address.[/red]\n")
        return None

def validate_target(target):
    domain_pattern = re.compile(r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$")
    ip_pattern = re.compile(r"^(?:\d{1,3}\.){3}\d{1,3}$")
    return bool(domain_pattern.match(target) or ip_pattern.match(target))

def choose_recon_mode():
    console.print("\n[bold green]Choose Recon Mode:[/bold green]")
    console.print("[1] Passive Recon - No active interaction (WHOIS, OSINT)")
    console.print("[2] Quiet Active Recon - Slower scans, reduced noise")
    console.print("[3] Normal Active Recon - Full scans without restrictions")
    
    while True:
        choice = console.input("\n[bold green]Enter your choice (1-3):[/bold green] ").strip()
        if choice == "1":
            console.print("[cyan]Passive Recon selected![/cyan]")
            return "Passive Recon"
        elif choice == "2":
            console.print("[cyan]Quiet Active Recon selected![/cyan]")
            return "Quiet Active Recon"
        elif choice == "3":
            console.print("[cyan]Normal Active Recon selected![/cyan]")
            return "Normal Active Recon"
        else:
            console.print("[red]Invalid choice! Please enter 1, 2, or 3.[/red]")

def execute_recon(target, selected_modules, recon_mode):
    console.print(f"[bold yellow]Running recon on {target} in {recon_mode} mode...[/bold yellow]")
    for module in selected_modules:
        with console.status(f"[cyan]Executing {module}...[/cyan]"):
            time.sleep(1)  # Simulate module execution
        console.print(f"[bold green]{module} completed![/bold green]")
    console.print("[bold green]Recon completed![/bold green]\n")

def select_modules():
    console.print("\n[bold green]Select the recon modules to run:[/bold green]")
    console.print("[1] DNS Recon\n[2] Port Scanning\n[3] Web Directory Brute-forcing\n[4] OSINT Recon\n[0] Done\n")
    
    selected_modules = []
    while True:
        choice = console.input("> ").strip()
        if choice == "1" and "DNS Recon" not in selected_modules:
            with console.status("[cyan]Selecting DNS Recon...[/cyan]"):
                time.sleep(0.5)
            selected_modules.append("DNS Recon")
            console.print("[bold cyan]DNS Recon selected![/bold cyan]")
        elif choice == "2" and "Port Scanning" not in selected_modules:
            with console.status("[cyan]Selecting Port Scanning...[/cyan]"):
                time.sleep(0.5)
            selected_modules.append("Port Scanning")
            console.print("[bold cyan]Port Scanning selected![/bold cyan]")
        elif choice == "3" and "Web Directory Brute-forcing" not in selected_modules:
            with console.status("[cyan]Selecting Web Directory Brute-forcing...[/cyan]"):
                time.sleep(0.5)
            selected_modules.append("Web Directory Brute-forcing")
            console.print("[bold cyan]Web Directory Brute-forcing selected![/bold cyan]")
        elif choice == "4" and "OSINT Recon" not in selected_modules:
            with console.status("[cyan]Selecting OSINT Recon...[/cyan]"):
                time.sleep(0.5)
            selected_modules.append("OSINT Recon")
            console.print("[bold cyan]OSINT Recon selected![/bold cyan]")
        elif choice == "0":
            break
        else:
            console.print("[red]Invalid or duplicate choice! Please try again.[/red]")
    
    return selected_modules

def main():
    target = None
    recon_mode = None
    selected_modules = []
    
    while True:
        choice = main_menu(target, recon_mode, selected_modules)
        
        if choice == "1":
            target = set_target()
        elif choice == "2":
            selected_modules = select_modules()
        elif choice == "3":
            recon_mode = choose_recon_mode()
        elif choice == "4":
            if target and selected_modules and recon_mode:
                execute_recon(target, selected_modules, recon_mode)
            else:
                console.print("[red]Please set a target, choose recon mode, and select at least one module before executing recon![/red]\n")
        elif choice == "5":
            console.print("[yellow]Viewing reports coming soon...[/yellow]\n")
        elif choice == "0":
            console.print("[bold red]Exiting...[/bold red]")
            break
        else:
            console.print("[red]Invalid choice! Please try again.[/red]\n")

if __name__ == "__main__":
    main()
