# awk 'BEGIN{FS=",";OFS="|";}{
#     print($2,$3,$4,$5)
# }' fruits.txt

# grep -i "[Aa]pple" fruits.txt| awk 'BEGIN{FS=",";sum=0;print("\t\tMethod1");}
# {
#     sum+=$5
#     # print($2)
# }
# END{print("Total amount spent on Apple is",sum)}'

# awk 'BEGIN{FS=",";sum=0;print("\t\tMethod 2");}
# {
#     # print($2)
#     if($2=="Apple" || $2=="apple")
#     {
#         sum=sum+$5
#         # print("In the loop",$2)
#     }
# }
# END{
#     if(sum!=0){
#         print("Total amount spent on Apple is",sum)
#         # print(sum)
#     }
#     else{
#         print("Did not buy any Apple")
#     }
# }' fruits.txt


# awk 'BEGIN{FS=",";}
# {
#     print("Number of records in ",NR-1," is ",NF)
# }' fruits.txt

awk 'BEGIN{FS=",";OFS="|";i=0;}
{
    # # Even number of lines
    # if(NR%2==0){
    #     print(NR,$0)
    # # fields in a single lines
    #     print(NF)
    # # Last row of every line
    #     print($NF)
    # }
    # Square of first 5 numbers
    ++i
    print("Square of i",i*i)

}' fruits.txt