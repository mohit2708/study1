
### Table of Contents

|  No.  | Questions                                                                                                                                      |
| :---: | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|       | [What is angular?](#ques-What-is-angular)                                                                                                      |
|       | [What is the difference between AngularJS and Angular?](#ques-What-is-the-difference-between-AngularJS-and-Angular)                            |
|       | [What is NPM?](#ques-What-is-NPM)                                                                                                              |
|       | [What is CLI Tool?](#ques-What-is-CLI-Tool)                                                                                                    |
|       | [What is TypeScript?](#ques-What-is-TypeScript)                                                                                                |
|       | [What are Single Page Applications (SPA)?](#ques-What-are-Single-Page-Applications-(SPA))                                                      |
|       | [What is a bootstrapping module?](#ques-What-is-a-bootstrapping-module)                                                                        |
|       | [What are the key components of Angular?](#ques-What-are-the-key-components-of-Angular)                                                        |
|       | [What are component?](#ques-What-are-component)                                                                                                |
|       | [Create the component?](#ques-Create-the-component)                                                                                            |
|       | [Create model?](#Create-model)                                                                                                                 |
|       | [What are Templates in Angular?](#ques-What-are-Templates-in-Angular)                                                                          |
|       | [What is metadata?](#ques-What-is-metadata)                                                                                                    |
|       | [What are directives?](#ques-What-are-directives)                                                                                              |
|       | [How to create custome directive?](#ques-How-to-create-custome-directive)                                                                      |
|       | [What is data binding?](#ques-What-is-data-binding)                                                                                            |
|       | [What is Two Way Binding in Angular?](#ques-What-is-Two-Way-Binding-in-Angular)                                                                |
|       | [What are decorators in Angular?](#ques-What-are-decorators-in-Angular)                                                                        |
|       | [What is Selector and Templates?](#ques-What-is-Selector-and-Templates)                                                                        |
|       | [What are Pipes in Angular?](#ques-What-are-Pipes-in-Angular)                                                                                  |
|       | [What is Chaining Pipes?](#ques-What-is-Chaining-Pipes)                                                                                        |
|       | [Creating Custom Pipes?](#ques-Creating-Custom-Pipes)                                                                                          |
|       | [What are Pure Pipes?](#ques-What-are-Pure-Pipes)                                                                                              |
|       | [What are Impure Pipes?](#ques-What-are-Impure-Pipes)                                                                                          |
|       | [What exactly is a parameterized pipe?](#ques-What-exactly-is-a-parameterized-pipe)                                                            |
|       | [Difference between Pure and Impure pipes?](#ques-Difference-between-Pure-and-Impure-pipes)                                                    |
|       | [What are Annotations in Angular?](#ques-What-are-Annotations-in-Angular)                                                                      |
|       | [What is an ngModule?](#ques-What-is-an-ngModule)                                                                                              |
|       | [What is the scope in angularJs?](#ques-What-is-the-scope-in-angularJs)                                                                        |
|       | [Diffrence between doller scope and $rootScope?](#ques-Diffrence-between-doller-scope-and-rootScope)                                           |
|       | [What is Eager and Lazy loading?](#ques-What-is-Eager-and-Lazy-loading)                                                                        |
|       | [How are observables different from promises?](#ques-How-are-observables-different-from-promises)                                              |
|       | [What are RxJs in Angular?](#ques-What-are-RxJs-in-Angular)                                                                                    |
|       | [What are lifecycle hooks in Angular? Explain a few lifecycle hooks?](#ques-What-are-lifecycle-hooks-in-Angular-Explain-a-few-lifecycle-hooks) |
|       | [What is ngOnInit?](#ques-What-is-ngOnInit)                                                                                                    |
|       | [What are router links?](#ques-What-are-router-links)                                                                                          |
|       | [What exactly is the router state?](#ques-What-exactly-is-the-router-state)                                                                    |
|       | [What does Angular Material means?](#ques-What-does-Angular-Material-means)                                                                    |
|       | [What is transpiling in Angular?](#ques-What-is-transpiling-in-Angular)                                                                        |
|       | [What are HTTP interceptors?](#ques-What-are-HTTP-interceptors)                                                                                |
|       | [What is AOT compilation What are the advantages of AOT?](#ques-What-is-AOT-compilation-What-are-the-advantages-of-AOT)                        |
|       | [What is Webpack?](#ques-What-is-Webpack)                                                                                                      |





### Ques. What is angular?
* Angular is a **TypeScript-based open-source** front-end platform that makes it easy to build web/mobile/desktop application development framework created by Google. 
* It is used to build frontend, single-page applications that run on JavaScript.

### Ques. What is the difference between AngularJS and Angular?
| AngularJS                                       | Angular                                                  |
| ----------------------------------------------- | -------------------------------------------------------- |
| It is supports javascript                       | It support both javascript and TypeScript                |
| It is based on MVC architecture                 | This is based on Service/Controller based a architecture |
| It uses use JavaScript to build the application | It Uses TypeScript to build the application              |
| It does not have CLI tool                       | It has CLI Tool                                          |
| Based on controllers concept                    | This is a component based UI approach                    |
| It does not use Dependency Injection.           | It uses Dependency Injection.                            |
| No support for mobile platforms                 | Fully supports mobile platforms                          |
| Difficult to build SEO friendly application     | Ease to build SEO friendly applications                  |

### Ques. What is NPM?
* NPM package manage is an online repository from where you can get thousend of free library.
* NPM stands for Node Package Manager, responsible for managing all the packages and modules for Node.js.
  
### Ques. What is CLI Tool?
* Angular CLI helps developers to create projects easily and quickly.
* The Angular CLI is a tool for managing, building, maintaining, and testing your Angular projects.
* CLI is a command-line interface tool that you use to initialize, develop, scaffold, and maintain Angular applications directly from a command shell.
* **Install the Angular CLI**
```javascript
npm install -g @angular/cli
```
* install the **specific version** of angular-cli.
```javascript
npm install -g @angular/cli@12
```
* Check the version of angular cli
```javascript
ng version
```

### Ques. What is TypeScript?
* TypeScript is an object-oriented strongly typed language.
* TypeScript is a strongly typed superset of JavaScript created by Microsoft that adds optional types, classes, async/await and many other features, and compiles to plain JavaScript.
* We can install TypeScript globally.
```javascript
npm install -g typescript
```

### Ques. What are Single Page Applications (SPA)?
* A single page application is a website or web application that dynamically rewrites a current web page with new data from the web server, instead of the default method of a web browser loading entire new pages.

### Ques. What is a bootstrapping module?
* Bootstrapping is the process of initializing or loading our Angular application.
* The process of loading the index. html page, app-level module, and app-level component is called bootstrapping, or loading the app.
* **Angular takes the following steps to load our first view.**
  1. Loads Index.html
  2. Loads Angular & Third-party libraries & Application
  3. Executes application entry point (main.ts)
  4. Load & execute Root Module (app.module.ts)
  5. Executes the Root Component (app.component.ts)
  6. Displayes the template (app.component.html)

### Ques. What are the key components of Angular?
Angular has the key components below.
1. **Component:** These are the basic building blocks of an Angular application to control HTML views.
2. **Modules:** An Angular module is a set of angular basic building blocks like components, directives, services etc. An application is divided into logical pieces and each piece of code is called as "module" which perform a single task.
3. **Templates:** These represent the views of an Angular application.
4. **Services:** Are used to create components which can be shared across the entire application.
5. **Metadata:** This can be used to add more data to an Angular class.
6. **Directives:** Add extra behavior to existing elements or add new elements.
7. **Pipes:** Add responsible for formatting data in templates.


### Ques. What are component?
* Components are the most basic UI building block of an Angular app which formed a tree of angular components.
* These components are associated with a template and are a subset of directives. 

### Create the component?
```javascript
ng generate component login (OR)
ng g c component_name 
```

### Create model
* Modules are logical boundaries in your application and the application is divided into saprate modules to saparate the functinality of our application.
* It is a place where you can group the components, directives, Pipes and services, which are related to the application.
```javascript
# Create model
ng g m user_auth
```
* create component in model
```javascript
ng g c user_auth/login
```

### Ques. What are Templates in Angular?
* A template is a form of HTML that tells Angular how to render the component.
* Angular Templates are written with HTML that contains Angular-specific elements and attributes. In combination with the model and controller's information, these templates are further rendered to provide a dynamic view to the user.
* **There are two ways to create a template in an Angular component:**
  * **Inline Template:** The component decorator's template config is used to specify an inline HTML template for a component. The Template will be wrapped inside the single or double quotes.
  ```javascript
    @Component({
      selector: "app-greet",
      template: `<div>
          <h1> Hello {{name}} how are you ? </h1>
          <h2> Welcome to interviewbit ! </h2>
      </div>`
    })
  ```

  * **Linked Template:**  A component may include an HTML template in a separate HTML file. As illustrated below, the templateUrl option is used to indicate the path of the HTML template file.
  ```javascript
    @Component({
      selector: "app-greet",
      templateUrl: "./component.html"
    })
  ```

### Ques. What is services?
* A services is a typescript class and a reusable code which can be used in multipal components.
* Service can be implemented with the help of dependency injection.
```javascript
ng genrate service service_name
```

### Ques. What is metadata?
* Metadata is used to decorate a class so that it can configure the expected behavior of the class. Following are the different parts for metadata.


### Ques. What are directives?
* Directives are classes that add additional behavior to elements in your Angular applications. Multipal directives can be applied to single Dom element.
* Directive are elements which change the appearance or behavior of the DOM elements.
* Directive in angular can be categorized into the following types:
1. **Component Directive:-** 
   * It is mainly used to specify the html templates.
   * These form the main class in directives. Instead of @Directive decorator we use @Component decorator to declare these directives. These directives have a view, a stylesheet and a selector property.
    ```javascript
        @Component({
          selector: 'app-root',
          templateUrl: './app.component.html',
          styleUrls: ['./app.component.css']
        })
    ```

2. **Structural Directive:-** 
* Structural directives are used to change the DOM layout by adding and removing DOM elements. It basically changes the structure of the DOM
Examples of structural directives are **ngIf**, **ngFor**, **ngSwitch**.
* These directives are generally used to manipulate DOM elements.
* All structural Directives are preceded by Asterix **(*)** symbol.
  * ***ngIf —** adds or removes element from DOM.
  * ***ngFor —** renders list of elements on every iteration.
```javascript
  <div *ngIf="isReady" class="display_name">
      {{name}}
  </div>


  <div class="details" *ngFor="let x of details" >
      <p>{{x.name}}</p>
      <p> {{x.address}}</p>
      <p>{{x.age}}</p>
  </div>
```
3. **Attribute directive:-** 
* Attribute directives are used to change the look and behaviour of a DOM element. Let’s understand attribute directives by creating one.
* Attribute directives are used to change the appearance or behavior of an element.
* Examples of attributes directives are **ngStyle**, **ngClass**, **ngModel**
  * **ngStyle —** used to apply styles that will change the appearance.
  * **ngClass —** used to apply CSS classes to change the appearance.


### Ques. How to create custome directive?
```javascript
ng g directive name_of_the_directive
```

### Ques. What is data binding?
* Data binding in AngularJS is the synchronization between the model and the view.
* When data in the model changes, the view reflects the change, and when data in the view changes, the model is updated as well.
* We can make connections in **two different ways** one way and two-way binding.

* **One-way data binding** is a one-way interaction between component and its template. If you perform any changes in your component, then it will reflect the HTML elements. It supports the following types −
  * **String interpolation:-** Interpolation is used to display data from component to view (DOM). It is denoted by the expression of {{ }} and also known as **mustache** syntax.
    1. String interpolations can work on string type only, not number or any other type.
    2. It is reprsented inside {{data}} double curly braces.
  ```javascript
    # login.components.ts

    export class LoginComponent {
      title = "hello Word!";
    }

    # login.components.html

    <div>{{title}}</div>
  ```
  * **Property binding:-** Property binding is used to bind the data from property of a component to DOM elements. It is denoted by [].
  1.  it can set an element property to a non-string data value like boolean.
    ```javascript
     <div [innerText]='title'></div>
    ```
  * **Event binding:-** Events are actions like mouse click, double click, hover or any keyboard and mouse actions. If a user interacts with an application and performs some actions, then event will be raised. It is denoted by either parenthesis () or on-
    ```javascript
    <button (click)="clickFunction()">Submit</button>
    ```

### Ques. What is Two Way Binding in Angular?
* Two-way data binding in angular will help users to exchange data from the view to component and then from component to the view at the same time.
```javascript
{{title}}
<input type="text" [(ngModel)]="title">
```

### Ques. What are decorators in Angular?
* Decorators are a design pattern that is used to separate modification or decoration of a class without modifying the original source code.
* In AngularJS, decorators are functions that allow a service, directive, or filter to be modified before it is used.
* **There are four main types of angular decorators:**
  * **Class decorators**, such as **@Component** and **@NgModule**
  * **Property decorators** for properties inside classes, such as **@Input** and **@Output**
  * **Method decorators** for methods inside classes, such as **@HostListener**
  * **Parameter decorators** for parameters inside class constructors, such as **@Inject**




### Ques. What is Selector and Templates?
* A **Selector** is used to identify each component uniquely into the components tree.
* A Templates is a HTML view of angular component.
```javascript
# app.component.ts

import { Component } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {
  title = "hello login page1";
  alertfunction(){
    alert("hello dost");
  }
}
```


### Ques. What are Pipes in Angular? 
* Pipes are simle function which accept an input value and return a transformed value.
* Pipes are simply a function that we can directly apply on any expression/value in a template to transform it into some other value.
* **Some key features include:**
  * Pipes are defined using the pipe “|” symbol. 
  * Pipes can be chained with other pipes.
  * Pipes can be provided with arguments by using the colon ( : ) sign.
* **Some commonly used predefined Angular pipes are:**
  * DatePipe: Formats a date value.
  * UpperCasePipe: Transforms text to uppercase.
  * LowerCasePipe: Transforms text to lowercase.
  * CurrencyPipe: Transforms a number to the currency string.
  * PercentPipe: Transforms a number to the percentage string. 
  * DecimalPipe: Transforms a number into a decimal point string.
```javascript
<h3>{{title | upercase}}</h3>
```

### Ques. What is Chaining Pipes?
* The Chaining Pipes use multiple pipes on a data input.
```javascript
<h3>{{dob | date | uppercase}}</h3> -> JUL 23, 1984
```

### Ques. Creating Custom Pipes?

### Ques. What are Pure Pipes?
* Pure pipes in angular are the pipes that execute when it detects a pure change in the input value.
* A pure change is when the change detection cycle detects a change to either a primitive input value (such as String, Number, Boolean, or Symbol) or object reference (such as Date, Array, Function, or Object). 

### Ques. What are Impure Pipes?
* An impure pipe is called for every change detection cycle no matter whether the value or parameters changes. i.e An Impure pipe is called often, as often as every keystroke or 

### Ques. What exactly is a parameterized pipe?
* A pipe can receive any number of optional parameters. The parameterized pipe is constructed by first stating the pipe name followed by a colon (:) and then the parameter value.


### Ques. Difference between Pure and Impure pipes?
| Pure Pipe                                                                                 | Impue Pipe                                                                                          |
| ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| The pipe is executed only when it detects a change in primitive value or object reference | The pipe is executed on every change detection cycle irrespective of the change in the input value. |
| A single instance is created.                                                             | Multiple instances are created                                                                      |
| It uses pure function                                                                     | It uses an impure function                                                                          |
| Pure pipe optimizes application performances.                                             | Impure pipe may slow down your application                                                          |



### Ques. What are Annotations in Angular?

### Ques. What is an ngModule?
* NgModules are containers that reserve a block of code to an application domain or a workflow.
* 



### Ques. What is the scope in angularJs?
* The scope is an object with the available properties and methods.
* The scope is the binding part between the HTML (view) and the JavaScript (controller).
* The scope is available for both the view and the controller.
```javascript
<div ng-app="myApp" ng-controller="myCtrl">

<h1>{{carname}}</h1>

</div>

<script>
var app = angular.module('myApp', []);

app.controller('myCtrl', function($scope) {
  $scope.carname = "Volvo";
});
</script>
```

### Ques. Diffrence between doller scope and $rootScope?
* A property assigned with **doller scope** cannot be used outside the controller in which it is defined whereas a property assigned with **$rootScope** can be used anywhere.
* $rootScope like a global varibale.
* The rootScope is available in the entire application.
* $scope like a local varibale.
```javascript
<!DOCTYPE html>
<html>
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.9/angular.min.js"></script>
<body>

<div ng-app="myApp">
  
  <div ng-controller="myCtrl">
	  <h1>{{carname}}</h1>
  </div>
  
    <div ng-controller="myCtrl1">
 	 <h1>{{name}}</h1> 	 <h1>{{msg1}}</h1>

  </div>
  
</div>

<script>
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope,$rootScope) {
    $scope.carname = "Volvo";
    $rootScope.msg1 = "hello myctrl"
});
app.controller('myCtrl1', function($scope,$rootScope) {
    $scope.name = "mohit";
    $rootScope.msg2 = "hello myctrl one"
});
</script>


</body>
</html>
```

### Ques. What is Eager and Lazy loading?
* **Loading:** The eager loading technique is the default module-loading strategy. Eager loading feature modules are loaded before the program begins. This is primarily utilized for small-scale applications.
* **Lazy Loading:** Lazy loading loads the feature modules dynamically as needed. This speeds up the application. It is utilized for larger projects where all of the modules are not required at the start.

### Ques. How are observables different from promises?* 
* The first difference is that an Observable is **lazy** whereas a Promise is **eager**.



### Ques. What are RxJs in Angular?
* The full form of RxJS is **Reactive Extension for Javascript**.
* It is a javascript library that uses observables to work with reactive programming that deals with asynchronous data calls, callbacks and event-based programs.

### Ques. What are lifecycle hooks in Angular? Explain a few lifecycle hooks?
* Every component in Angular has a lifecycle, and different phases it goes through from the time of creation to the time it's destroyed.1. Constructor
2. ngOnchange
3. ngOnInit
4. ngDoCheck   
   1. ngAfterContentInit   
   2. ngAfterContentChecked   
   3. ngAfterViewInit
   4. ngAfterviewChecked5.
5. ngOnDestroy

### Ques. What is ngOnInit?
* ngOnInit is a lifecycle hook and callback function used by Angular to mark the creation of a component. It accepts no arguments and returns a void type.
```javascript
export class MyComponent implements OnInit {
constructor() { }
    ngOnInit(): void {
        //....
    }
}
```

### Ques. What are router links?
* RouterLink is an anchor tag directive that gives the router authority over those elements. Because the navigation routes are set.

### Ques. What exactly is the router state?
* RouterState is a route tree.
* It tells how the various components of an application are arranged on the screen to define what should be displayed on it.


### Ques. What does Angular Material means?
Angular Material is a user interface component package that enables professionals to create a uniform, appealing, and fully functioning websites, web pages, and web apps. It does this by adhering to contemporary web design concepts such as gentle degradation and browser probability.


### Ques. What is transpiling in Angular?
Transpiling is the process of transforming the source code of one programming language into the source code of another. Typically, in Angular, this implies translating TypeScript to JavaScript. TypeScript (or another language like as Dart) can be used to develop code for your Angular application, which is subsequently transpiled to JavaScript. This occurs naturally and internally.

### Ques. What are HTTP interceptors?
Using the HttpClient, interceptors allow us to intercept incoming and outgoing HTTP requests. They are capable of handling both HttpRequest and HttpResponse. We can edit or update the value of the request by intercepting the HTTP request, and we can perform some specified actions on a specific status code or message by intercepting the answer.


### Ques. What is AOT compilation? What are the advantages of AOT?
* Every Angular application consists of components and templates that the browser cannot understand. Therefore, all the Angular applications need to be compiled first before running inside the browser.
* **Angular provides two types of compilation:**
1. JIT(Just-in-Time) compilation
2. AOT(Ahead-of-Time) compilation

### Ques. What is AOT Compilation?
* Ahead-of-Time (AOT), which compiles your app at build time.
* The Angular ahead-of-time (AOT) compiler converts your Angular HTML and TypeScript code into efficient JavaScript code during the build phase before the browser downloads and runs that code.

### Ques. What is JIT Compilation?
* Just-in-Time (JIT), which compiles your app in the browser at runtime.

### Ques. Differance between Ahead of Time (AOT) and Just in Time (JIT)?
| JIT                                                                                            | AOT                                                                                                               |
| ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| JIT downloads the compiler and compiles code exactly before Displaying in the browser.         | AOT has already complied with the code while building your application, so it doesn’t have to compile at runtime. |
| Loading in JIT is slower than the AOT because it needs to compile your application at runtime. | Loading in AOT is much quicker than the JIT because it already has compiled your code at build time.              |
| JIT is more suitable for development mode.                                                     | AOT is much suitable in the case of Production mode.                                                              |
| Bundle size is higher compare to AOT.                                                          | Bundle size optimized in AOT, in results AOT bundle size is half the size of JIT bundles.                         |
| You can run your app in JIT with this command: **ng build OR ng serve**                        | To run your app in AOT you have to provide –aot at the end like: **ng build --aot OR ng serve --aot**             |
| You can catch template binding error at display time.                                          | You can catch the template error at building your application.                                                    |


### Ques. What is Webpack?
* Webpack is a bundler. it scans our application looking for javascript files and merges them into one ( or more) big file. Webpack has the ability to bundle any kind of file like JavaScript, CSS, SASS, LESS, images, HTML, & fonts, etc.
* The Angular CLI uses Webpack as a module bundler. Webpack needs a lot of configuration options to work correctly. The Angular CLI sets up all these configuration options behind the scene.
* The Webpack traverses through our application, looking for javascript and other files, and merges all of them into one or more bundles. In our example application, it has created five files.


### Ques. What is form in angular?
* Forms are used to handle user input data. Angular supports two types of forms. They are **Template driven forms** and **Reactive forms**.

### Template driven forms:- 
* A form value can be generated using the “form.value” object. Form data is exported as JSON values when the submit method is called. 
* Basic HTML validations can be used to validate the form fields. In the case of custom validations, directives can be used. 
* Controls can be added to the form using the NGModel tag. Multiple controls can be grouped using the NGControlGroup module. 
* Template driven forms is created using directives in the template. It is mainly used for creating a simple form application.

### Reactive forms:-
* With Reactive forms, the component directly manages the data flows between the form controls and the data models
* Reactive forms are code-driven, unlike the template-driven approach.
* Reactive forms eliminate the anti-pattern of updating the data model via two-way data binding.
* Typically, Reactive form control creation is synchronous and can be unit tested with synchronous programming techniques. 

### Ques. Difference between Reactive Forms and Template-driven Forms?
| Comparison Index   | Reactive Forms                                                         | Template-driven Forms                                                    |
| ------------------ | ---------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Setup (form model) | Reactive forms are more explicit. They are created in component class. | Template-driven forms are less explicit. They are created by directives. |
| Data model         | Structured                                                             | Unstructured                                                             |
| Predictability     | Synchronous                                                            | Asynchronous                                                             |
| Form validation    | Functions                                                              | Directives                                                               |
| Mutability         | Immutable                                                              | Mutable                                                                  |
| Scalability        | Low-level API access                                                   | Abstraction on top of APIs                                               |

### Ques. Similarity between Reactive Forms and Template-driven Forms
* FormControl: It is used to track the value and validation status of an individual form control.
* FormGroup: It is used to track the same values and status for a collection of form controls.
* FormArray: It is used to track the same values and status for an array of form controls.
* ControlValueAccessor: It is used to create a bridge between Angular FormControl instances and native DOM elements.



### Ques. Download the node?
* Go to the url:- https://nodejs.org/en/
* Check the version of node:- open the cmd and run this commend:- **node -v**
* check the version of npm:- **npm -v**

### Ques. Create the project?
```javascript
node --version
npm --version

ng new my_first_project
cd my-first-project
ng serve
```

### Folder Structure?
* package.json
* src
    * app
    * assets:- css, js, img
    * favicon.ico
    * index.html
    * main.ts
    * styles.scss
* angular.json:- project ki configration


### HostListener
* It is a decorater which gets applied over a function and its trigger that function whenever that event occures.