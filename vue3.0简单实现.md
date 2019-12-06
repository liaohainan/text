```js
// vue3.0 响应式原理
// 1.) 2.0 默认会递归 2).数组改变length 是无效的 3） 对象不存在的属性不能被拦截
// 判断是不是对象
// proxy  兼容性差 ie11 不兼容
let toProxy = new WeakMap(); // 弱引用映射表 es6  放置的是 原对象:代理过的对象
let toRaw  = new WeakMap(); // 被代理过的对象:原对象  es6语法
// mdn每个api 都过一遍
function isObject(val){
    return typeof val === 'object' && val !== null;
}
function hasOwn(target,key){
    return target.hasOwnProperty(key);
}
// 1.响应式的核心方法
function reactive(target){
    // 创建响应式对象 
    return createReativeObject(target);
}
// 创建响应式对象的
function createReativeObject(target){
    if(!isObject(target)){ // 如果当前不是对象 直接返回即可
        return target;
    }
    let proxy = toProxy.get(target); // 如果已经代理过了 就将代理过的结果返回即可
    if(proxy){
        return proxy;
    }
    if(toRaw.has(target)){ // 放置代理的过的对象再次被代理
        return target;
    }
    let baseHandler = { 
        // reflect 优点 不回报错 而且 会有返回值 会替代掉Object 上的方法
        get(target,key,receiver){
            // proxy + reflect 反射
            let result = Reflect.get(target,key,receiver);
            // result 是当前获取到的值

            // 收集依赖 订阅 把当前的key 和 这个effect 对应起来

            track(target,key); // 如果目标上的 这个key 变化了 重新让数组中的effect执行即可
            return isObject(result)?reactive(result):result; // 是个递归
        },
        set(target,key,value,receiver){ // [1,2,3,4]
            // 怎么去 识别是改属性 还是 新增属性
            let hadKey = hasOwn(target,key); // 判断这个属性 以前有没有
            let oldValue = target[key];
            let res = Reflect.set(target,key,value,receiver);
            if(!hadKey){
                trigger(target,'add',key);
            }else if(oldValue !== value){ // 这里表述属性 更改过了
                trigger(target,'set',key);
            } // 为了屏蔽 无意义的修改
            // 如果设置没成功 如果这个对象不可以被更改 writable
            return res;
        },
        deleteProperty(target,key){
            let res = Reflect.deleteProperty(target,key)
            console.log('删除')
            return res;
        }
    }
    let observed = new Proxy(target,baseHandler); //es6
    toProxy.set(target,observed);
    toRaw.set(observed,target);
    return observed;
}
// 栈 先进后出  {name:[effect]}
let activeEffectStacks = []; // 栈型结果
// {
//     target:{
//         key:[fn,fn]
//     }
// }
let targetsMap = new WeakMap(); // 集合和hash表
function track(target,key){ // 如果这个tagret中的 key 变化了 我就执行数组里的方法
    let effect = activeEffectStacks[activeEffectStacks.length-1];
    if(effect){ // 有对应关系 才创建关联
        let depsMap = targetsMap.get(target);
        if(!depsMap){
            targetsMap.set(target,depsMap = new Map);
        }
        let deps = depsMap.get(key);
        if(!deps){
            depsMap.set(key,deps = new Set())
        }
        if(!deps.has(effect)){
            deps.add(effect);
        } 
        // 动态创建依赖关系
    }
    // 什么都不做
}
function trigger(target,type,key){
    let depsMap = targetsMap.get(target);
    if(depsMap){
        let deps = depsMap.get(key);
        if(deps){ // 将当前key 对应的effect 依次执行
            deps.forEach(effect => {
                effect();
            });
        }
    }
}

// 响应式 副作用
function effect(fn){
    // 需要把fn这个函数编程响应式的函数
    let effect = createReactiveEffect(fn);
    effect(); // 默认应该先执行一次
}
function createReactiveEffect(fn){
    let effect = function (){ // 这个就是创建的响应式的effect
        return run(effect,fn); // 运行 1.让fn执行，第二个就是把这个effect存到栈中
    }
    return effect;
}
function run(effect,fn){ // 运行fn 并且将effect 存起来
    try{
        activeEffectStacks.push(effect);
        fn(); // vue2 利用了js是单线程的
    }finally{
        activeEffectStacks.pop();
    }
}
// 依赖收集 发布订阅
let obj = reactive({name:'zf'});
effect(()=>{ // effect 会执行两次 ,默认先执行一次 之后依赖的数据变化了 会再次执行
    console.log(obj.name); // 会调用get方法
})
obj.name = 'jw'

// ref computed
// 代理对象 
// let arr = [1,2,3];
// let proxy = reactive(arr);
// proxy.length = 100;

// let object = {name:{n:'z'}}
// let proxy = reactive(object); // 多层代理 通过get方法 来判断
// // 需要记录一下 如果这个对象代理过了 就不要在new了
// // hash表 映射表
// let proxy = reactive(proxy); 
// reactive(object); 

```
