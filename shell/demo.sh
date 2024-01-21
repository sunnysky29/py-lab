

:<<!

# 注释内容块

echo "-------------------CUP占用前10排序--------------------------------"
ps -eo user,pid,pcpu,pmem,args --sort=-pcpu  |head -n 10
echo "-------------------内存占用前10排序--------------------------------"
ps -eo user,pid,pcpu,pmem,args --sort=-pmem  |head -n 10

!

###################################################################################

fruits=("Apple" "Banana" "Orange" "Mango")

echo ${fruits[0]}  # 输出0元素----> Apple

length=${#fruits[@]}  # 输出列表长度
echo "The length of the array is: $length"  # 4

# 使用for循环遍历数组
for fruit in "${fruits[@]}"; do
    echo "I like $fruit"
done

for i in {1..4}; do 
    echo ${i}; 
done

echo "====================================="

for file in $(ls ./); do echo ${file}; done  # 文件列表循环
command=$(nvidia-smi)
for i in "${command[@]}"; do
    echo "$i -------" >& a.log
done

echo "====================================="

URL_LIST="www.baidu.com www.ctnrs.com www.der-matech.net.cn www.der-matech.com.cn www.der-matech.cn www.der-matech.top www.der-matech.org"
for URL in $URL_LIST; do
    echo "URL is $URL"
done

echo "====================================="

lyList=("wang" "xiao" "hui")
for ly in ${lyList[@]}; do
    echo "$ly, @@" >> a.log  # >> 追加写入
done

echo "====================================="
function submit {
    user=$1
    mess=$2
    echo "name=$user & con=$mess"

}

submit lss 234  # name=lss & con=234
submit ${lyList[@]} # name=wang & con=xiao


echo "===========# 传递数组=========================="

a=(1 2)
b=(3 4 6)

function multi {
    a=$1
    b=$2
    for a1 in $a; do
        for b1 in $b; do
            val=`expr $a1 \* $b1`
            echo "$a1 x $b1 = $val"
        done 
    done


}
multi "${a[*]}" "${b[*]}"  # 传递数组



