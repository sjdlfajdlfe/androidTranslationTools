# androidTranslationTools
android 上使用的多语言处理工具。

1.支持 xls 转 xml。
  一般情况下，运营部或者其它部门将string 传到线上的excel上，所以我们需要支持，xls 到xml的转换。
  
2. 支持 format strings。
  生成xml 后，有很多字符和android strings.xml 规则不一致。所以我们需要format。
  
3. 支持merge
  每次新生成的文件需要和旧文件merge，便于更新。

