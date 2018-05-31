grammar Expressions;

start : expr ;

expr : left=expr op=('*'|'/') right=expr
      | left=expr op=('+'|'-') right=expr
      | atom=INT
;

INT : ('0'..'9')+ ;

WS : [ \r\t\n]+ -> skip;