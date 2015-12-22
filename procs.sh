for i in $(ps -aux | awk '{print $11}')
do  
  firstl=`echo $i | cut -c1`
  if [ $firstl == "/" ]; then
    `md5sum $i >> checkfile.txt`
  fi
done

for j in $(find /lib/* -type f)
do
  echo `md5sum $j >> checkfile.txt`
done
