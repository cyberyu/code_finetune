#!/usr/bin/env python3
"""
Command-line interface for refact_utils.scripts
"""
import sys
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
        prog='python -m refact_utils.scripts',
        description='Refact Utils Scripts - Various utility scripts for model processing'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Lora Merger subcommand
    lora_parser = subparsers.add_parser(
        'merge-lora', 
        help='Merge LoRA weights into base model'
    )
    lora_parser.add_argument(
        'model_path', 
        type=str, 
        help='Path to the base model (e.g., codellama/CodeLlama-7b-hf)'
    )
    lora_parser.add_argument(
        'checkpoint_path', 
        type=Path, 
        help='Path to the LoRA checkpoint directory'
    )
    lora_parser.add_argument(
        'output_filename', 
        type=Path, 
        help='Output filename for the merged model (will be a .zip file)'
    )
    
    if len(sys.argv) == 1:
        parser.print_help()
        return
    
    args = parser.parse_args()
    
    if args.command == 'merge-lora':
        from .merge_lora import LoraMerger
        
        try:
            merger = LoraMerger(args.model_path)
            merger.lora_patch_save(args.checkpoint_path, args.output_filename)
            print(f"Successfully merged LoRA weights and saved to: {args.output_filename}")
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
