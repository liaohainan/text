
## 安装依赖
```
npm install --save-dev @babel/preset-typescript @typescript-eslint/eslint-plugin @typescript-eslint/parser eslint-plugin-typescript ts-loader typescript
```


## 更改webpack配置，增加ts-loader


事实上如果整个库都已经更改为ts后，就不需要babel-loader了，但是如果是混合 项目，则仍旧需要babel
```js


rules: [
      {
        test: /\.tsx?$/,
        use: {
            loader: 'ts-loader'
        }
      },
```
更改entry


```
*.js => *.ts
```


## 增加tsconfig.json
```json
{
    "compilerOptions": {
        "charset": "utf8",
        "sourceMap": true,
        "allowSyntheticDefaultImports": true,
        "declaration": true, // 生成声明文件，开启后会自动生成声明文件
        "declarationDir": "./@types",
        "target": "es5", // 目标
        "module": "es6",
        "outDir": "./build",
        "experimentalDecorators": true,
        "moduleResolution": "node",
        "removeComments": false,
        "preserveConstEnums": true,
        "allowJs": true,
        "lib": ["es6", "dom"],
        "baseUrl": ".",
        "paths": {
            "@/*": ["./src/*"]
        }
    },
    "include": ["base/**/*","src/**/*","utils/*/*"],
    "exclude": ["node_modules", "config", "test", "lib", "babel"]
}



```


## babel配置增加@babel/preset-typescript,是为了让jest识别ts文件


```js
"presets": ["@babel/preset-env","@babel/preset-typescript"],
```




## 增加ts-lint


后续补充


## 更改js为ts


按照ts规范增加类型，更改错误等

## other

如果要把ts文件先过ts-loader，再走babel-loader则需要改配置

```js

{
        test: /\.ts(x?)$/,
        exclude: /node_modules/,
        use: [
          {
            loader: 'babel-loader'
          },
          {
            loader: 'ts-loader'
          }
        ]
      },
```
或者
那就使用webpack的 preLoaders 先处理ts，loaders 来操作 babel。














