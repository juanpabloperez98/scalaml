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
(* val tupla1 = (4,2.0,#"A");
val tupla2 = (8,"Hola mundo",#"B");
val tupla3 = (20,true,#"C");
val resultado = #3(tupla1) + # *)

(* EJEMPLO1 SECCION4 *)
(* val num = 3;
fun cube(x:int) = x*x*x;
cube(num); *)


(* EJEMPLO2 SECCION4 *)
(* val tupla = (1,2,3);
fun lesser_to_numbers(x,y) = 
    if x < y then x else y;
fun lesser(x,y,z) = 
    lesser_to_numbers(lesser_to_numbers(x,y),z);
lesser(tupla); *)


(* EJEMPLO3 SECCION4 *)
(* val lista = [1,2,3];
fun reverse xs =
    hd(tl(tl(xs))) :: hd(tl(xs)) :: hd(xs) :: nil;
reverse(lista); *)

(* EJEMPLO4 SECCION4 *)
(* val precio1 = 20000.0;
val precio2 = 40000.0;
val precio3 = 60000.0;
fun app_iva(x:real) =
    x + x * 0.19;
app_iva(precio1);
app_iva(precio2);
app_iva(precio3); *)


(* EJEMPLO1 SECCION5 *)
(* val x = 3
fun factorial(x) =
    if x = 1 then
        1
    else
        factorial(x-1)*x;
factorial(x); *)