from src.parsers.cron_syntax import parse_simple_cron_fields
def test_cron_syntax():
    res = parse_simple_cron_fields('30 2 * * *')
    assert res['minute'] == '30'
    assert res['hour'] == '2'
