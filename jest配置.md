# 二、Jest 配置
虽然说Jest是零配置，但也是可以配置
## （一）配置位置
- 1. package.json
在package.json添加配置项"jest" : { 配置项 }
- 2. jest.config.js
新建jest.config.js并添加配置项module.exports = { 配置项 }
- 3. 命令行（独有的option）
见：命令行配置
## （二）配置项
- 1. testMatch
设置识别哪些文件是测试文件（glob形式），与testRegex互斥，不能同时写
```
testMatch: ['\*\*/\_\_tests\_\_/\*\*/\*.js?(x)','\*\*/?(*.)(spec|test).js?(x)']
```
- 2. testRegex
设置识别哪些文件是测试文件（正则形式），与testMatch互斥，不能同时写
```
testRegex: '(/\_\_tests\_\_).*|(\\\\.|/)(test|spec))\\\\.jsx?$'
```
- 3. testRnviroment
测试环境，默认值是：jsdom，可修改为node
```
testEnvironment: 'jsdom'
```
- 4. rootDir
默认值：当前目录，一般是package.json所在的目录。
rootDir: ' '

- 5. moduleFileExtensions
测试文件的类型
```
moduleFileExtensions: ['js','json','jsx','node']
```
一般配置：
```js
module.exports = {
    testMatch: ['<rootDir>/test/\*\*/\*.js'],
    testEnvironment: 'jsdom',
    rootDir: '',
    moduleFileExtensions: ['js','json','jsx','node']
}
```
