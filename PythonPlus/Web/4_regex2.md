# 正则表达式
此段为markdown，建议在编辑器里面查看
## 概述
`^[0-9]+abc$`  
`^` 为匹配输入字符串的开始位置  
[0-9]+ 匹配多个数字， [0-9] 匹配单个数字， + 匹配一个或多个  
  
我们在写用户注册表单时，只允许用户名包含字符、数字、下划线和连接字符(-)，
并设置用户名的长度，我们就可以使用以下正则表达式来设定  
`^[a-z0-9_-]{3-15}$`  
匹配包含 a-z 0-9 _- 的 长度为3-15的字符串  
例如： mute mutexd1 , 不可行： mutexD m1 mute@
## 语法
`mutex+d` 可以匹配 mutexd mutexxd mutexxxxxxd  + 号代表前面的字符必须至少出现一次  
`mutex*d` 可以匹配 muted mutexxd mutexxxxxxxd  * 号代表前面的字符可以不出现，也可以出现一次或者多次（0次、或1次、或多次）  
`colou?r`  可以匹配 color colour ? 问号代表前面的字符最多只可以出现一次（0次、或1次）  
  
正则表达式是由普通字符（例如字符 a 到 z）以及特殊字符（称为"元字符"）组成的文字模式。
模式描述在搜索文本时要匹配的一个或多个字符串。
正则表达式作为一个模板，将某个字符模式与所搜索的字符串进行匹配  
  
**普通字符**  
普通字符包括没有显式指定为元字符的所有可打印和不可打印字符。
这包括所有大写和小写字母、所有数字、所有标点符号和一些其他符号  
**非打印字符**  
非打印字符也可以是正则表达式的组成部分，如下表所示
  
|字符|描述|
|----|----|
|`\cx`|匹配由x指明的控制字符。例如， \cM 匹配一个 Ctrl-M 或回车符。x 的值必须为 A-Z 或 a-z 之一。否则，将 c 视为一个原义的 'c' 字符|
|`\f`|匹配一个换页符。等价于 \x0c 和 \cL|
|`\n`|匹配一个换行符。等价于 \x0a 和 \cJ|
|`\r`|匹配一个回车符。等价于 \x0d 和 \cM|
|`\s`|匹配任何空白字符，包括空格、制表符、换页符等等。等价于 `[\f\n\r\t\v]`。注意 Unicode 正则表达式会匹配全角空格符|
|`\S`|匹配任何非空白字符。等价于 `[^\f\n\r\t\v]`|
|`\t`|匹配一个制表符。等价于 \x09 和 \cI|
|`\v`|匹配一个垂直制表符。等价于 \x0b 和 \cK|
**特殊字符**  
特殊字符就是一些有特殊含义的字符，如上面说的 `mutex*d` 中的 `*`，
简单的说就是表示任何字符串的意思。如果要查找字符串中的 `*` 符号，则需要对 `*` 进行转义，
即在其前加一个 `反斜杠` 即 `mute\*xd` 匹配 `mute*xd`  
  
许多元字符要求在试图匹配它们时特别对待。若要匹配这些特殊字符，必须首先使字符"转义"，
即，将反斜杠字符`反斜杠`放在它们前面。下表列出了正则表达式中的特殊字符
  
|特别字符|描述|
|---|---|
|`$`|匹配输入字符串的结尾位置。如果设置了正则对象的多行匹配属性，则 $ 也匹配 '\n' 或 '\r'。要匹配 $ 字符本身，请使用`反斜杠$`|
|`( )`|标记一个子表达式的开始和结束位置。子表达式可以获取供以后使用。要匹配这些字符，请使用`反斜杠（`和`反斜杠）`|
|`*`|匹配前面的子表达式零次或多次|
|`+`|匹配前面的子表达式一次或多次|
|`.`|匹配除换行符 \n 之外的任何单字符|
|`[`|标记一个中括号表达式的开始|
|`?`|匹配前面的子表达式零次或一次，或指明一个非贪婪限定符|
|`\`|将下一个字符标记为或特殊字符、或原义字符、或向后引用、或八进制转义符|
|`^`|匹配输入字符串的开始位置，除非在方括号表达式中使用，当该符号在方括号表达式中使用时，表示不接受该方括号表达式中的字符集合|
|`{`|标记限定符表达式的开始|
|`|`|指明两项之间的一个选择|
  
**限定符**  
限定符用来指定正则表达式的一个给定组件必须要出现多少次才能满足匹配  
有` *  +  ?  {n}  {n,}  {n,m}` 共6种  

|特别字符|描述|
|---|---|
|`*`|匹配前面的子表达式零次或多次。例如，`zo*` 能匹配 "z" 以及 "zoo"。* 等价于`{0,}`|
|`+`|匹配前面的子表达式一次或多次。例如，`zo+` 能匹配 "zo" 以及 "zoo"，但不能匹配 "z"。+ 等价于 `{1,}`|
|`?`|匹配前面的子表达式零次或一次。例如，`do(es)?` 可以匹配 "do" 、 "does" 中的 "does" 、 "doxy" 中的 "do". ?等价于 `{0,1}`|
|`{n}`|n 是一个非负整数。匹配确定的 n 次。例如，`o{2}` 不能匹配 "Bob" 中的 'o'，但是能匹配 "food" 中的两个 o|
|`{n,}`|n 是一个非负整数。至少匹配n 次。例如，`o{2,}` 不能匹配 "Bob" 中的 'o'，但能匹配 "foooood" 中的所有 o。'o{1,}' 等价于 'o+'。'o{0,}' 则等价于 'o*'|
|`{n,m}`|m 和 n 均为非负整数，其中n <= m。最少匹配 n 次且最多匹配 m 次。例如，`o{1,3}` 将匹配 "fooooood" 中的前三个 o。`o{0,1}` 等价于 'o?'。请注意在逗号和两个数之间不能有空格|

`/[1-9][0-9]*/`  
此正则表达式匹配一个正整数，`[1-9]`设置第一个数字不是 0，`[0-9]*` 表示任意多个数字  
`/[0-9]{1,2}/`  
匹配0~99 的两位数 但只能匹配两位数字，而且可以匹配 0、00、01、10 99 的章节编号仍只匹配开头两位数字  
`/[1-9][0-9]?/` or `/[1-9][0-9]{0,1}/` 上面的改进版  
`*`和 `+` 限定符都是贪婪的，因为它们会尽可能多的匹配文字，只有在它们的后面加上一个 ? 就可以实现非贪婪或最小匹配
  
匹配 `<h1>Mute-Tiny Blog</h1>`  
贪婪： `/<.*>/` 将匹配整个字符串  
非贪婪： `/<.*?>/` or `/<\w+?>/` 匹配`<h1>`  
通过在 *、+ 或 ? 限定符之后放置 ?，该表达式从"贪婪"表达式转换为"非贪婪"表达式或者最小匹配

**定位符**  
定位符使您能够将正则表达式固定到行首或行尾。它们还使您能够创建这样的正则表达式，这些正则表达式出现在一个单词内、在一个单词的开头或者一个单词的结尾  

|字符|描述|
|---|---|
|`^`|匹配输入字符串开始的位置。如果设置了 RegExp 对象的 Multiline 属性，^ 还会与 \n 或 \r 之后的位置匹配|
|`$`|匹配输入字符串结尾的位置。如果设置了 RegExp 对象的 Multiline 属性，$ 还会与 \n 或 \r 之前的位置匹配|
|`\b`|匹配一个单词边界，即字与空格间的位置|
|`\B`|非单词边界匹配|

`/^Chapter [1-9][0-9]{0,1}$/`  
章节标题不仅出现行的开始处，而且它还是该行中仅有的文本。它即出现在行首又出现在同一行的结尾，通过创建只匹配一行文本的开始和结尾的正则表达式，就可做到这一点  
`/\bCha/` 和 `/ter\b/` 匹配单词 Chapter 的开头三个字符 和 结尾三个字符  
`/\Bapt/` 表达式匹配 Chapter 中的字符串 apt，但不匹配 aptitude 中的字符串 apt

**反向引用**  
对一个正则表达式模式或部分模式两边添加圆括号将导致相关匹配存储到一个临时缓冲区中，所捕获的每个子匹配都按照在正则表达式模式中从左到右出现的顺序存储。缓冲区编号从 1 开始，最多可存储 99 个捕获的子表达式。每个缓冲区都可以使用 \n 访问，其中 n 为一个标识特定缓冲区的一位或两位十进制数  
可以使用非捕获元字符 ?:、?= 或 ?! 来重写捕获，忽略对相关匹配的保存  
  
反向引用的最简单的、最有用的应用之一，是提供查找文本中两个相同的相邻单词的匹配项的能力  
`/\b([a-z]+) \1\b/ig`
* [a-z]+ 指定的，包括一个或多个字母  
* 正则表达式的第二部分是对以前捕获的子匹配项的引用
* \1 指定第一个子匹配项
* 单词边界元字符 /b 确保只检测整个单词
* 正则表达式后面的全局标记 `g` 指定将该表达式应用到输入字符串中能够查找到的尽可能多的匹配
* 表达式的结尾处的不区分大小写 `i` 标记指定不区分大小写
* 多行标记指定换行符的两边可能出现潜在的匹配  
I`m Mute, **a a** noob.  
  
`/(\w+):\/\/([^/:]+)(:\d*)?([^# ]*)/`
* 第一个括号子表达式捕获 Web 地址的协议部分。该子表达式匹配在冒号和两个正斜杠前面的任何单词
* 第二个括号子表达式捕获地址的域地址部分。子表达式匹配非 : 和 / 之后的一个或多个字符
* 第三个括号子表达式捕获端口号（如果指定了的话）。该子表达式匹配冒号后面的零个或多个数字。只能重复一次该子表达式
* 第四个括号子表达式捕获 Web 地址指定的路径和 / 或页信息。该子表达式能匹配不包括 # 或空格字符的任何字符序列
## 元字符
下表包含了元字符的完整列表以及它们在正则表达式上下文中的行为

|字符|描述|
|---|---|
|`\`|将下一个字符标记为一个特殊字符、或一个原义字符、或一个 向后引用、或一个八进制转义符。例如，'n' 匹配字符 "n"。'\n' 匹配一个换行符|
|`^`|匹配输入字符串的开始位置。如果设置了 RegExp 对象的 Multiline 属性，^ 也匹配 '\n' 或 '\r' 之后的位置|
|`$`|匹配输入字符串的结束位置。如果设置了RegExp 对象的 Multiline 属性，$ 也匹配 '\n' 或 '\r' 之前的位置|
|`*`|匹配前面的子表达式零次或多次|
|`+`|匹配前面的子表达式一次或多次|
|`?`|匹配前面的子表达式零次或一次|
|`{n}`|n 是一个非负整数。匹配确定的 n 次|
|`{n,}`|n 是一个非负整数。至少匹配 n 次|
|`{n,m}`|m 和 n 均为非负整数，其中n <= m。最少匹配 n 次且最多匹配 m 次|
|`?`|当该字符紧跟在任何一个其他限制符 (*, +, ?, {n}, {n,}, {n,m}) 后面时，匹配模式是非贪婪的。非贪婪模式尽可能少的匹配所搜索的字符串，而默认的贪婪模式则尽可能多的匹配所搜索的字符串|
|`.`|匹配除换行符（\n、\r）之外的任何单个字符|
|`(pattern)`|匹配 pattern 并获取这一匹配|
|`(?:pattern)`|匹配 pattern 但不获取匹配结果，也就是说这是一个非获取匹配，不进行存储供以后使用|
|`(?=pattern)`|正向肯定预查，在任何匹配pattern的字符串开始处匹配查找字符串。这是一个非获取匹配，也就是说，该匹配不需要获取供以后使用|
|`(?!pattern)`|正向否定预查，在任何不匹配pattern的字符串开始处匹配查找字符串。这是一个非获取匹配，也就是说，该匹配不需要获取供以后使用|
|`(?<=pattern)`|反向肯定预查，与正向肯定预查类似，只是方向相反|
|`(?<!pattern)`|反向否定预查，与正向否定预查类似，只是方向相反|
|`x丨y`|匹配 x 或 y|
|`[xyz]`|字符集合。匹配所包含的任意一个字符|
|`[^xyz]`|负值字符集合。匹配未包含的任意字符|
|`[a-z]`|字符范围。匹配指定范围内的任意字符|
|`[^a-z]`|负值字符范围。匹配任何不在指定范围内的任意字符|
|`\b`|匹配一个单词边界，也就是指单词和空格间的位置|
|`\B`|匹配非单词边界|
|`\cx`|匹配由 x 指明的控制字符|
|`\d`|匹配一个数字字符|
|`\D`|匹配一个非数字字符|
|`\f`|匹配一个换页符|
|`\n`|匹配一个换行符
|`\r`|匹配一个回车符|
|`\s`|匹配任何空白字符，包括空格、制表符、换页符等等|
|`\S`|匹配任何非空白字符|
|`\t`|匹配一个制表符|
|`\v`|匹配一个垂直制表符|
|`\w`|匹配字母、数字、下划线|
|`\W`|匹配非字母、数字、下划线|
|`\xn`|匹配 n，其中 n 为十六进制转义值。十六进制转义值必须为确定的两个数字长|
|`\num`|匹配 num，其中 num 是一个正整数。对所获取的匹配的引用|
|`\n`|标识一个八进制转义值或一个向后引用。如果 \n 之前至少 n 个获取的子表达式，则 n 为向后引用。否则，如果 n 为八进制数字 (0-7)，则 n 为一个八进制转义值|
|`\nm`|标识一个八进制转义值或一个向后引用。如果 \nm 之前至少有 nm 个获得子表达式，则 nm 为向后引用。如果 \nm 之前至少有 n 个获取，则 n 为一个后跟文字 m 的向后引用|
|`\nml`|如果 n 为八进制数字 (0-3)，且 m 和 l 均为八进制数字 (0-7)，则匹配八进制转义值 nml|
|`\un`|匹配 n，其中 n 是一个用四个十六进制数字表示的 Unicode 字符。例如， \u00A9 匹配版权符号 (?)|
## 优先级
正则表达式从左到右进行计算，并遵循优先级顺序，这与算术表达式非常类似  
相同优先级的从左到右进行运算，不同优先级的运算先高后低。下表从最高到最低说明了各种正则表达式运算符的优先级顺序  

|运算符|描述|
|---|---|
|`\` |	转义符|
|`(), (?:), (?=), []`|圆括号和方括号|
|`*, +, ?, {n}, {n,}, {n,m}`|限定符|
|`^, $, \任何元字符、任何字符`|定位点和序列（即：位置和顺序）|
|`|`|替换"或"操作， 字符具有高于替换运算符的优先级，使得"m丨food"匹配"m"或"food"|
## 匹配规则
**基本模式匹配**  

`^once` 只匹配那些以once开头的字符串  
`bucket$` 与"buckets"不匹配  
`^bucket$` 字符 ^ 和 $ 同时使用时，表示精确匹配（字符串与模式一样）,只匹配字符串"bucket"  

**字符簇**

|字符簇|描述|
|---|---|
|`[AaEeIiOoUu]`|任何元音字符|
|`[a-z]`|所有的小写字母|
|`[A-Z]`|匹配所有的大写字母|
|`[a-zA-Z]`|匹配所有的字母|
|`[0-9`]|匹配所有的数字|
|`[0-9\.\-]`|匹配所有的数字，句号和减号|
|`[ \f\r\t\n]`|匹配所有的白字符|
|`[^a-z]`|除了小写字母以外的所有字符|
|`[^\\\/\^]`|除了(\\)(/)(^)之外的所有字符|
|`[^\"\']`|除了双引号(")和单引号(')之外的所有字符|

**确定重复出现**

|字符簇|描述|
|---|---|
|`^[a-zA-Z_]$`|所有的字母和下划线|
|`^a$`|字母a|
|`^a{4}$`|aaaa|
|`^a{2,4}$`|aa,aaa或aaaa|
|`^a{1,3}$`|a,aa或aaa|
|`^a{2,}$`|包含多于两个a的字符串|
|`^a{2,}`|如：aardvark和aaab，但apple不行|
|`a{2,}`|如：baad和aaa，但Nantucket不行|
|`\t{2}`|两个制表符|
|`.{2}`|所有的两个字符|
* 一个数字`{x}`的意思是前面的字符或字符簇只出现x次
* 一个数字加逗号`{x,}`的意思是前面的内容出现x或更多的次数
* 两个数字用逗号分隔的数字`{x,y}`表示 前面的内容至少出现x次，但不超过y次  

例如

|字符簇|描述|
|---|---|
|`^[a-zA-Z0-9_]{1,}$`|所有包含一个以上的字母、数字或下划线的字符串|
|`^[1-9][0-9]{0,}$`|所有的正整数|
|`^\-{0,1}[0-9]{1,}$`|所有的整数|
|`^[-]?[0-9]+\.?[0-9]+$`|所有的浮点数|

最后一个例子：  
* 以一个可选的负号 `([-]?)` 开头 `(^)`
* 跟着1个或更多的数字`([0-9]+)`
* 和一个小数点`(\.)`
* 再跟上1个或多个数字`([0-9]+)`
* 并且后面没有其他任何东西`($)`
* 特殊字符`?`与`{0,1}`是相等的，它们都代表着：0个或1个前面的内容 或 前面的内容是可选的  

上表可转化为：
|字符簇|描述|
|---|---|
|`^[a-zA-Z0-9_]+$`|所有包含一个以上的字母、数字或下划线的字符串|
|`^[1-9][0-9]*$`|所有的正整数|
|`^\-?[0-9]+$`|所有的整数|
|`^[-]?[0-9]+(\.[0-9]+)?$`|所有的浮点数|