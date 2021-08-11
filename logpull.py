import time
import subprocess
import pathlib
import argparse
import rich.console as rcon

console = rcon.Console()

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t', '--target', type=str, default='./',
        help='Targfet directory. The logfiles are stored here.'
    )
    parser.add_argument(
        '-i', '--interval', type=int, default=90,
        help='The interval time between data file updates in seconds.'
    )
    args = parser.parse_args()

    target_dir = pathlib.Path(args.target)
    interval = args.interval

    ctr = 0

    with console.status('[bold green]Waiting interval ...') as status:
        while True:
            pull_logdir(targetdir=target_dir)
            time.sleep(interval)
            ctr += 1
            console.log(f'Pulled {ctr} times')

    return None

def pull_logdir(targetdir: str) -> None:
    HOST = 'vingilot'
    PATH = '/home/ext/datalab1/datadir/trainrun_aug/logs'

    retout = subprocess.run(
        ['scp', '-r', ':'.join((HOST, PATH)), targetdir],
        capture_output=True
    )
    # console.print(retout, style='bold red')
    return None


if __name__ == '__main__':
    console.print('helloooorz45z45zreto', style='bold red')
    print('itsa meee')

    main()
