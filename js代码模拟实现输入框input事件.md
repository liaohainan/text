一些时候我们要做网页插件时往往需要去做很多输入框自动赋值,去实现对应功能.
随着web前端发展,MVVM框架的流行,很多页面想要实现自动赋值不再向以前那样对输入框简单的赋值即可,还需要对应的触发相关的事件让对应框架去取值才行.
一般情况下,最常见的就是发送输入框input事件了,(如vue的v-model本身就是自动帮你绑定了input事件去取值)
这里简单封装了一个方法.
```js
window.___inputValue = function (dom, st) {
  var evt = new InputEvent('input', {
    inputType: 'insertText',
    data: st,
    dataTransfer: null,
    isComposing: false
  });
  dom.value = st;
  dom.dispatchEvent(evt);
}
简单的调用:

window.___inputValue(document.querySelector('input'),'输入要赋值的内容')
```
这方面的资料相对较少,这里记录一下以便将来需要用到时查阅方便.
