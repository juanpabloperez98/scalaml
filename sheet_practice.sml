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

(* EJEMPLO3 SECCION3 *)
(* val tupla1 = (2.0,11,"Programacion");
val tupla2 = (#"A","en",20 div 2);
val tupla3 = ("ML",2+1,20 div 2);
val concat_ = #3(tupla1) :: #2(tupla2) :: #1(tupla3) :: nil;
val concat_result = concat(concat_); *)


(* EJEMPLO4 SECCION3 *)
(* val lista = [1,1,2,123];
val mayor = 0;
val element_first = hd(lista);
val element_second = hd(tl(lista));
val element_third = hd(tl(tl(lista)));
val element_four = hd(tl(tl(tl(lista))));
val mayor = if mayor < element_first then element_first else mayor;
val mayor = if mayor < element_second then element_second else mayor;
val mayor = if mayor < element_third then element_third else mayor;
val mayor = if mayor < element_four then element_four else mayor; *)


(* EJEMPLO5 SECCION3 *)
val lista = [4,3,2,1];
val mayor = 0;
val element_first = hd(lista);
val element_second = hd(tl(lista));
val element_third = hd(tl(tl(lista)));
val element_four = hd(tl(tl(tl(lista))));
val mayor = if mayor < element_first then element_first else mayor;
val mayor = if mayor < element_second then element_second else mayor;
val mayor = if mayor < element_third then element_third else mayor;
val mayor = if mayor < element_four then element_four else mayor;
if mayor = element_first then 1 
else 
    if mayor = element_second then 2
    else
        if mayor = element_third then 3
        else
            if mayor = element_four then 4 else mayor



