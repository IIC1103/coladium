from string import Template

LOGIN = 'https://intrawww.ing.puc.cl/siding/index.phtml'
CATALOG = ('https://intrawww.ing.puc.cl'
           '/siding/dirdes/ingcursos/cursos/index.phtml'
           '?acc_inicio=catalogo')
STUDENT_LIST = Template('https://intrawww.ing.puc.cl/siding/dirdes/ingcursos'
                        '/cursos/index.phtml?accion_curso=alumnos&acc_alumnos'
                        '=mostrar_lista&id_curso_ic=${section_id}&agrupar_repetidos')
