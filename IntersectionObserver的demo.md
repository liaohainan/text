基础组件Card
```js
import React, {Component} from 'react';

export default class Card extends Component{
    constructor(props){
        super(props)
        
    }

    
    render(){
        let img_css = {
            width: '200px',
            height: '200px'
        }
        return(
            <div className={'img'} {...this.props} ref={(ref=>{this.ref=ref})}>
                    <img style={img_css} src="https://yanxuan-item.nosdn.127.net/e6b4ea84c67b8da854e7073294eb3e1a.png" alt=""/>
            </div>
        )
    }
}
```

List组件
```js
import React, { Component } from "react";
import Card from "./Card";
import SpmView from "./SpmView";

let CardA = SpmView(Card);
let list_style ={
    display:'flex',
    flexWrap:'wrap'

}
export default class List extends Component {
  constructor(props) {
    super(props);
    this.arr = [1, 2, 3, 4, 5, 56,6,63,6356,637357,3637375,5373736,36354,63747];
  }
  render() {
    return (
      <div style={list_style}>
        {this.arr.map(e => {
          return <CardA key={e}  area={'area'} b={'bbbbb'}/>;
        })}
      </div>
    );
  }
}
```


曝光组件
```js
import React, { Component } from "react";
const SpmView = (ContentComponent) => {
  return class extends Component {
    constructor(props) {
      super(props);
      this.myRef = React.createRef();
      this.observer = null
    }
    init() {
      // let box = document.querySelectorAll('.box');
      // console.log(box)
      this.observer = new IntersectionObserver(entries => {
        console.log(`发生交叉行为，目标元素有${entries.length}个`);
        console.log("发生曝光行为");
        
      });

      // box.forEach(item => observer.observe(item)); // 监听多个box
      let item = this.myRef.current.ref;
      this.observer.observe(item);
    }
    componentDidMount() {
      this.init();
    }
    componentWillUnmount(){
      this.observer.disconnect()
      this.observer = null
    }
    render() {
      return <ContentComponent {...this.props} ref={this.myRef} />;
    }
  };
};

export default SpmView;



```
