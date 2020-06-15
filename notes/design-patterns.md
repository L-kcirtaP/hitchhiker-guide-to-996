## 设计模式

### 创建型

- **简单工厂模式 Single Factory Pattern**

  - 又称静态工厂。

  - 定义一个抽象基类，根据不同参数创建不同子类的实例。

  - Role: Factory (工厂类，实现创建逻辑), Product (抽象父类，公共接口), ConcreteProduct (创建类的实例)

    ```
    #include "Factory.h"
    #include "ConcreteProductA.h"
    #include "ConcreteProductB.h"
    Product* Factory::createProduct(string proname){
      if ( "A" == proname )
      {
        return new ConcreteProductA();
      }
      else if("B" == proname)
      {
        return new ConcreteProductB();
      }
      return  NULL;
    }
    ```

- **工厂方法模式 Factory Method Pattern**

  - 定义一个抽象工厂类，再定义具体工厂子类以完成实例创建过程。这样，如果出现新的产品子类，可以直接创建一个新的工厂子类而不必修改其他工厂。

  - Role: Product, ConcreteProduct, Factory, ConcreteFactory.

    ```
    #include "Factory.h"
    #include "ConcreteFactory.h"
    #include "Product.h"
    #include "ConcreteProduct.h"  
    #include <iostream>
    using namespace std;
    
    Product* ConcreteFactory::factoryMethod() {
      return  new ConcreteProduct();
    }
    
    int main(int argc, char *argv[])
    {
      Factory * fc = new ConcreteFactory();
      Product * prod = fc->factoryMethod();
      prod->use();
      
      delete fc;
      delete prod;
      
      return 0;
    }
    ```

  - 利用了OOP的**多态**性。

- **抽象工厂模式 Abstract Factory**

  - **提供一个创建一系列相关或相互依赖对象的接口**，而无须指定它们具体的类。

  - 抽象工厂模式与工厂方法模式最大的区别在于，工厂方法模式针对的是一个产品等级结构，而抽象工厂模式则需要面对多个产品等级结构，一个工厂等级结构可以负责多个不同产品等级结构中的产品对象的创建 。

  - Role: AbstractFactory, ConcreteFactory, AbstractProduct, Product

  - ```
      ///////////////////////////////////////////////////////////
    //  ConcreteFactory1.cpp
    //  Implementation of the Class ConcreteFactory1
    //  Created on:      02-十月-2014 15:04:11
    //  Original author: colin
    ///////////////////////////////////////////////////////////
    
    #include "ConcreteFactory1.h"
    #include "ProductA1.h"
    #include "ProductB1.h"
    AbstractProductA * ConcreteFactory1::createProductA(){
      return new ProductA1();
    }
    
    
    AbstractProductB * ConcreteFactory1::createProductB(){
      return new ProductB1();
    }
    ```

    ```
      ///////////////////////////////////////////////////////////
    //  ProductA1.cpp
    //  Implementation of the Class ProductA1
    //  Created on:      02-十月-2014 15:04:17
    //  Original author: colin
    ///////////////////////////////////////////////////////////
    
    #include "ProductA1.h"
    #include <iostream>
    using namespace std;
    void ProductA1::use(){
      cout << "use Product A1" << endl;
    }
    ```

    ```
    #include <iostream>
    #include "AbstractFactory.h"
    #include "AbstractProductA.h"
    #include "AbstractProductB.h"
    #include "ConcreteFactory1.h"
    #include "ConcreteFactory2.h"
    using namespace std;
    
    int main(int argc, char *argv[]) {
      AbstractFactory * fc = new ConcreteFactory1();
      AbstractProductA * pa =  fc->createProductA();
      AbstractProductB * pb = fc->createProductB();
      pa->use();
      pb->eat();
    
      AbstractFactory * fc2 = new ConcreteFactory2();
      AbstractProductA * pa2 =  fc2->createProductA();
      AbstractProductB * pb2 = fc2->createProductB();
      pa2->use();
      pb2->eat(); 
    }
    ```

### 行为型

### 结构型