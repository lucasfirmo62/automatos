from automata.fa.Moore import Moore

moore = Moore(['q0', 'q1', 'q2'],
['a' , 'b' , 'c'],
['0', '1'],
{
'q0' : {
'a' : 'q0',
'b' : 'q1',
'c' : 'q2'

},
'q1': {
'a' : 'q0',
'b' : 'q1',
'c' : 'q2'

},
'q2': {
'a' : 'q0',
'b' : 'q2',
'c' : ''

 },
 },

 'q0',
 {
 'q0' : '1',
 'q1' : '0',
 'q2' : '0',
 'q3' : '1'
 }
 )

print(moore)
print(moore.get_output_from_string('aabbaa'))