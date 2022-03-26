(* EJEMPLO1 SECCION 3 *)

(* val list1 = [1,2,3,4];
val list2 = [5,6,7,8];
val head_one = hd(list1);
val new_list = head_one :: tl(list2);
val element_first = hd(new_list);
val second_first = hd(tl(new_list));
val third_first = hd(tl(tl(new_list)));
val four_first = hd(tl(tl(tl(new_list))));
val suma = element_first + second_first + third_first + four_first *)


(* EJEMPLO2 SECCION 3 *)
(* val word = "Hola";
val convert_word = explode(word);
val firts_element = ord(hd(convert_word));
val second_first = ord(hd(tl(convert_word)));
val third_first = ord(hd(tl(tl(convert_word))));
val four_first = ord(hd(tl(tl(tl(convert_word)))));
val suma = firts_element + second_first + third_first + four_first; *)

(* EJEMPLO3 SECCION 3 *)
val tupla1 = (4,2.0,#"A");
val tupla2 = (8,"Hola mundo",#"B");
val tupla3 = (20,true,#"C");
val resultado = #3(tupla1) + #