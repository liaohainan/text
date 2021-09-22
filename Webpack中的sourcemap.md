### Webpack中sourcemap的配置

sourcemap是为了解决开发代码与实际运行代码不一致时帮助我们debug到原始开发代码的技术。尤其是如今前端开发中大部分的代码都经过编译，打包等工程化转换。比如开发环境下用scss写样式， 想在浏览器中在线编辑css那样编辑scss就不是那么容易了。从我自己看过的资料中， sourcemap的概念最早出现在12年， jquer1.9是较早支持sourcemap的库。这篇博客比较有代表性：[Introduction to JavaScript Source Maps](https://www.html5rocks.com/en/tutorials/developertools/sourcemaps/)，阮一峰的文章[JavaScript Source Map 详解](http://www.ruanyifeng.com/blog/2013/01/javascript_source_map.html)也大量参考该博客。关于sourcemap的原理及作用，基本在这两篇文章中讲清楚了。回到webpack中的sourcemap，就我这几天的琢磨， 这方面资料相对比较零散，但凡搜索Webpack中sourcemap的配置， 总是能得到千篇一律的如下信息：
Sourcemap type Quality Notes

> eval： 生成代码 每个模块都被eval执行，并且存在@sourceURL
> 
> cheap-eval-source-map： 转换代码（行内） 每个模块被eval执行，并且sourcemap作为eval的一个dataurl
> 
> cheap-module-eval-source-map： 原始代码（只有行内） 同样道理，但是更高的质量和更低的性能
> 
> eval-source-map： 原始代码 同样道理，但是最高的质量和最低的性能
> 
> cheap-source-map： 转换代码（行内） 生成的sourcemap没有列映射，从loaders生成的sourcemap没有被使用
> 
> cheap-module-source-map： 原始代码（只有行内） 与上面一样除了每行特点的从loader中进行映射
> 
> source-map： 原始代码 最好的sourcemap质量有完整的结果，但是会很慢

webpack中devtool的配置的官方文档在这 ：[webpack-devtool](https://webpack.github.io/docs/configuration.html#devtool)

## 疑问

反正我看完这些说明是云里雾里， 就我自己而言， 有3个疑问：

1.  eval和sourcemap有什么关系，eval模式是sourcemap吗？

2.  包含cheap关键字的配置中只有行内是什么意思？

3.  这几种不同的配置有什么区别？

## 解答

看似配置项很多， 其实只是五个关键字`eval`，`source-map`，`cheap`，`module`，`inline`的任意组合。这五个关键字每一项都代表一个特性， 这四种特性可以任意组合。它们分别代表以下五种特性（单独看特性说明有点不明所以，别急，往下看）：

*   eval： 使用eval包裹模块代码

*   source-map： 产生`.map`文件

*   cheap： 不包含列信息（关于列信息的解释下面会有详细介绍)也不包含loader的sourcemap

*   module： 包含loader的sourcemap（比如jsx to js ，babel的sourcemap）

*   inline： 将`.map`作为DataURI嵌入，不单独生成`.map`文件（这个配置项比较少见）

了解了以上各种不同特性， 再来逐一解答以上问题。

### eval和sourcemap有什么关系，eval模式是sourcemap吗？

`eval`和`source-map`都是webpack中devtool的配置选项，&nbsp;`eval`模式是使用`eval`将webpack中每个模块包裹，然后在模块末尾添加模块来源`//# souceURL`， 依靠`souceURL`找到原始代码的位置。包含eval关键字的配置项并不单独产生`.map`文件（eval模式有点特殊， 它和其他模式不一样的地方是它依靠sourceURL来定位原始代码， 而其他所有选项都使用`.map`文件的方式来定位）。包含`source-map`关键字的配置项都会产生一个`.map`文件，该文件保存有原始代码与运行代码的映射关系， 浏览器可以通过它找到原始代码的位置。（注：包含`inline`关键字的配置项也会产生`.map`文件，但是这个map文件是经过base64编码作为DataURI嵌入），举个栗子：`eval-source-map`是`eval`和`source-map`的组合，可知使用`eavl`语句包括模块，也产生了`.map`文件。webpack将`.map`文件作为DataURI替换`eval`模式中末尾的`//# souceURL`。按照我自己的理解，&nbsp;`eval`和`.map`文件都是sourcemap实现的不同方式，虽然大部分sourcemap的实现是通过产生`.map`文件， 但并不表示只能通过`.map`文件实现。下面是eval模式后产生的模块代码：
![](https://segmentfault.com/img/bVI3qw?w=741&amp;h=445)

### 包含cheap关键字的配置中只有行内是什么意思？

这里的列信息指的是代码的不包含原始代码的列信息。 官方文档对于包含`cheap`的解释是这样的：

```
> cheap-source-map - A SourceMap without **column-mappings**. SourceMaps
> from loaders are not used.
```

    这句话翻译过来就是“在cheap-source-map模式下sourcemap不包含列信息，也不包含loaders的sourcemap”这里的“column-mappings”就是代码列数的意思，是否包含loaders的sourcemap有什么区别将在之后提到。debug的时候大部分人都只在意代码的行数， 很少关注列数， 列数就是该行代码从第一个字符开始到定位字符的位置（包括空白字符）包含`cheap`关键字的模式不包含列信息，体现在webpack中就是：如果包含`cheap`关键字，则产生的`.map`文件不包含列信息。也就是说当你在浏览器中点击该代码的位置时， 光标只定位到行数，不定位到具体字符位置。而不包含`cheap`关键字时， 点击控制台log将会定位到字符位置。

    包含列信息后点击原始代码的定位，注意光标位置：
    ![](https://segmentfault.com/img/bVI3lF?w=677&amp;h=200)

    不包含列信息的光标位置：
    ![](https://segmentfault.com/img/bVI3qc?w=645&amp;h=235)

    这篇博客：[Go to a line number at a specific column](https://developers.google.com/web/updates/2015/05/go-to-a-line-number-at-a-specific-column)直观地展示了列数的概念。如果深入到webpack中的细节中体会该配置项，可以看这篇博客：[SurviveJS：Source Maps](http://survivejs.com/webpack/building-with-webpack/source-maps/)&nbsp;，该文章对比了webpack中所有配置项中`.map`文件的代码，这里截取`eval-source-map`和`cheap-source-map`的模式产生的`.map`文件代码中的`mappings`字段对比：

    devtool: 'eval-source-map'

 ```
 "mappings": "AAAAA,QAAQC,GAAR,CAAY,aAAZ",
 ```

    devtool: 'cheap-source-map'

```
"mappings": "AAAA",
```

注：这里使用了[VLQ编码](https://en.wikipedia.org/wiki/Variable-length_quantity)，（关于VLQ编码还可参考这里：[前端构建：Source Maps详解](http://www.cnblogs.com/fsjohnhuang/p/4208566.html)） 在VLQ编码中，逗号`,`表示字符列分割，分号`;`表示行分割。包含`cheap`关键字的配置项不包含列信息，也就没有逗号。关于VLQ编码， 本文最初的阮一峰的文章中有所解释。而不包含loader的sourcemap指的是不包含loader的sourcemap，不包含它时候如果你使用了诸如babel等代码编译工具时， 定位到的原始代码将是经过编译后的代码位置，而非原始代码。

比如当我用babel编译JS的时候，如果包含不包含loaders的sourcemap，此时debug到的将是编译后的代码， 而非原始代码，如图（这是使用cheap-source-map模式未包含loaders的sourcemap情况下的截图， debug的位置与之前的对比截图是同一个地方）：
![](https://segmentfault.com/img/bVI6aD?w=662&amp;h=411)

### 这几种不同的配置有什么区别？

通过以上两个问题的解释， webpack中的sourcemap各个配置项异同应该有了一定认识，乍看之下各个配置项很难记忆， 但其实从每个关键字所代表的特性入手， 就能体会到他们的异同。他们在webpack中的主要区别一个体现在重构的性能上， 总的来说`eval`性能最好，`source-map`性能最低，但就我自身的实践来看大多用的是最完整的`source-map`，该模式对于不管是js还是css，scss等都能很好的覆盖， 相反其他模式都不完整， 在开发环境下重构性能似乎比不上功能的完善。&nbsp;
另外需要补充的是`module`关键字， 当加上`module`关键字webpack将会添加loader的sourcemap。

