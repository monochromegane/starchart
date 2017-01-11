#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from ml import trainer, exposer, applyer

def main():
    parser = argparse.ArgumentParser(description='StarChart')
    subparsers = parser.add_subparsers()

    train_parser = subparsers.add_parser('train', help='Train model')
    train_parser.set_defaults(func=trainer.train)

    expose_parser = subparsers.add_parser('expose', help='Expose model')
    expose_parser.set_defaults(func=exposer.expose)

    apply_parser = subparsers.add_parser('apply', help='Apply model')
    apply_parser.set_defaults(func=applyer.apply)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
