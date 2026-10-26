from src.cli.args import get_parser
def test_cli():
    p = get_parser()
    args = p.parse_args(['status'])
    assert args.action == 'status'
