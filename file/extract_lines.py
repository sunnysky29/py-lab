
"""_summary_
该脚本用于从大型 JSONL 文件中提取前 N 行（默认 1000 行），
并保存到新文件，支持 命令行参数 或 默认路径。
不会全部加载整个大文件

python extract_jsonl.py 
    --input pretrain_hq.jsonl 
    --output pretrain_hq_1000.jsonl

"""

import argparse

def extract_lines(input_file, output_file, num_lines=1000):
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
            
        # enumerate(infile) 逐行读取，避免内存爆炸（适用于超大文件）。
        for i, line in enumerate(infile): 
            if i >= num_lines:
                break
            outfile.write(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='从大型JSONL文件中提取指定行数')
    parser.add_argument('--input', type=str, default='', 
                       help='输入JSONL文件路径，默认为空')
    parser.add_argument('--output', type=str, default='', 
                       help='输出JSONL文件路径，默认为空')
    parser.add_argument('-n', '--num_lines', type=int, default=1000,
                       help='要提取的行数，默认为1000')
    
    args = parser.parse_args()
    
    if not args.input or not args.output:
        print("错误：必须指定输入和输出文件路径")
        parser.print_help()
        exit(1)
    
    extract_lines(args.input, args.output, args.num_lines)
    print(f"已从 {args.input} 提取{args.num_lines}条数据到 {args.output}")