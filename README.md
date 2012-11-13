# Jgments #

A fork of Jgments (http://code.google.com/p/jgments/).

Jgments itself is a partial port of Pygments to Java.

## Why fork? ##

Using old Google jgments on large multiline comments will result `StackOverFlow` error
because of the limitation of `java.util.regex`. This version try to fixed these
errors by using `LexerAction` switching of original Pygments.

## How to use? ##
Clone this repo, and build a jar package with:

````bash
    ant jar
````

Copy generated `jgments.jar`, with all jars in `\lib`, to your classpath.
Then you can get all tokens in Java like:

````Java
    String filecontent="...";
    RegexLexerIterator iter = new RegexLexer(CppSyntax.INSTANCE, filecontent).iterator();
	while(iter.hasNext()){
		SyntaxSpan ss = iter.next();
        //...
    }
````

For more information, please visit original project page:
http://code.google.com/p/jgments/

## License ##

These works will follow the original license used in Google Jgments: the New
BSD license (http://opensource.org/licenses/BSD-3-Clause)

