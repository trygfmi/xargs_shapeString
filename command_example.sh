# ./command_example.sh


source ~/bashrc_folder/macports_alias
git clone https://github.com/trygfmi/xargs_shapeString
cd xargs_shapeString
find . -type f -name "*.txt"
find . -type f -name "*.txt" | xargs

