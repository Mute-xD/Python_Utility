New-Item testFolder -type directory -force
cd testFolder
New-Item testFile.py -type file -force -value "print('this is a test')"
New-Item .gitignore -type file -force -value "_pycache_/`n.idea/ "  # 居然不是 \n �?`n
echo "`nFile Create Success`n"
git init  # 创建git仓库
git status

git add .  # 添加所有文件进仓库
git status

git commit -m "Test Commit"  # 提交修改
git status
git log
echo '------------------------------------------------------------------------------------------------------------------------'
New-Item testFile.py -type file -force -value "print('this is a test')`nprint('a new line')"

git commit -am "A New Commit"
git status
git log
$response = git log --pretty=oneline| Out-String
$response -match "\n\w{6}"  # 正则提取前六位
New-Item testFile.py -type file -force -value "print('this is a test')`nprint('a new line')`nprint('this line should be removed')"

git status
git checkout .  # 检出到上次提交前

echo $Matches.Values[0]  # 提取第一次提交 ID
$input = Read-Host 'Copy the ID upper and paste here: '
git checkout $input
git checkout master
git status
git log
git reset --hard $input  # 放弃自指定提交之后的所有提交
git status
git log
# 重建git
echo '------------------------------------------------------------------------------------------------------------------------'
Remove-Item .git/* -Recurse -Force
git status
git init
git add .
git commit -m "A New Start"
git status

# clean up
cd ../ 
Remove-Item testFolder/ -Recurse -Force
echo "`n`nCleaning Success`n`n"
[System.Console]::Write('Press Any Key to Exit ...')
[void][System.Console]::ReadKey(1)
