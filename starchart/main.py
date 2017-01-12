#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from starchart.ml import trainer, stater, exposer, applyer

def main():
    parser = argparse.ArgumentParser(description='StarChart')
    subparsers = parser.add_subparsers()

    train_parser = subparsers.add_parser('train', help='Train model')
    train_parser.add_argument('--project-id',     help="Project ID.")
    train_parser.add_argument('--package-path',   help="Train program package path.")
    train_parser.add_argument('--module-name',    help="Train program module name.")
    train_parser.add_argument('--region',         help="Region.")
    train_parser.add_argument('args', nargs='*',  help="Train program parameters.")
    train_parser.set_defaults(func=trainer.train)

    state_parser = subparsers.add_parser('state',  help='State train job')
    state_parser.add_argument('--project-id',      help="Project ID.")
    state_parser.add_argument('--package-path',    help="Train program package path.")
    state_parser.set_defaults(func=stater.state)

    expose_parser = subparsers.add_parser('expose', help='Expose model')
    expose_parser.add_argument('--project-id',      help="Project ID.")
    expose_parser.add_argument('--package-path',    help="Train program package path.")
    expose_parser.set_defaults(func=exposer.expose)

    apply_parser = subparsers.add_parser('apply', help='Apply model')
    apply_parser.add_argument('--project-id',     help="Project ID.")
    apply_parser.add_argument('--package-path',   help="Train program package path.")
    apply_parser.set_defaults(func=applyer.apply)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
