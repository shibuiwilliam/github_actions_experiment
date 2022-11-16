import click

@click.command()
@click.option(
    "--test",
    type=str,
    default="aaaaaaaa",
)
def main(test: str):
    print("start")
    print(test)
    print("done")


if __name__ == "__main__":
    main()

