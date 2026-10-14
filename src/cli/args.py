import argparse
def get_parser():
    p = argparse.ArgumentParser(prog='cron-sentinel')
    sub = p.add_subparsers(dest='action')
    sub.add_parser('ping')
    sub.add_parser('wrap')
    sub.add_parser('status')
    return p
