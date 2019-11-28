方法使用

```js
// greetings.test.js
import { hello } from "./greetings";
import { current } from "./lang";

jest.mock("./lang", () => ({
  current: jest.fn(),
}));

describe("greetings", () => {
  describe("hello", () => {
    describe("when the language is set to galician", () => {
      it("returns galician for hi", () => {
        current.mockImplementation(() => "GL");
        expect(hello()).toEqual("Ola!");
      });
    });

    describe("when the language is not set to galician", () => {
      it("returns hi", () => {
        current.mockImplementation(() => "EN");
        expect(hello()).toEqual("Hi!");
      });
    });
  });
});
```

变量使用jest.mock,每次用每次都要mock，还要再使用的方法前边mock，有点麻烦

```js
// greetings.test.js
describe("greetings", () => {
  describe("hello", () => {
    describe("when the language is set to galician", () => {
      it("returns galician for hi", () => {
        jest.mock("./appEnv", () => ({ currentLanguage: "GL" }));
        const { hello } = require("./greetings");
        expect(hello()).toEqual("Ola!");
      });
    });

    describe("when the language is not set to galician", () => {
      it("returns hi", () => {
        jest.mock("./appEnv", () => ({ currentLanguage: "EN" }));
        const { hello } = require("./greetings");
        expect(hello()).toEqual("Hi!");
      });
    });
  });
});
```

https://medium.com/trabe/mocking-different-values-for-the-same-module-using-jest-a7b8d358d78b
