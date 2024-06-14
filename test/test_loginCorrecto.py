# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random

nombres = [
    'Alejandro', 'Maria', 'Pedro', 'Laura', 'Carlos', 'Ana', 'Jose', 'Sofia', 'Javier', 'Marta',
    'Luis', 'Juan', 'Antonio', 'Cristina', 'Elena', 'Ricardo', 'Fernando', 'Isabel', 'Miguel', 'Lucia',
    'Rafael', 'Sergio', 'Andrea', 'Carmen', 'Manuel', 'Nuria', 'Patricia', 'Sara', 'Jorge', 'Diego'
]

apellidos = [
    'Garcia', 'Martinez', 'Rodriguez', 'Lopez', 'Sanchez', 'Fernandez', 'Gomez', 'Diaz', 'Vazquez', 'Moreno',
    'Torres', 'Ruiz', 'Hernandez', 'Gutierrez', 'Ramirez', 'Jimenez', 'Molina', 'Castro', 'Ortega', 'Rubio',
    'Mendez', 'Alvarez', 'Romero', 'Gil', 'Medina', 'Vega', 'Rojas', 'Serrano', 'Iglesias', 'Navarro'
]

numero_aleatorio=1
class TestLoginCorrecto():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_loginCorrecto(self):
    self.driver.get("http://localhost:3001/login")
    self.driver.set_window_size(974, 1032)
    self.driver.find_element(By.ID, "input_email").click()
    self.driver.find_element(By.ID, "input_email").send_keys("jeremyaldama23.2@gmail.com")
    self.driver.find_element(By.ID, "input_password").click()
    self.driver.find_element(By.ID, "input_password").send_keys("edumentor")
    self.driver.find_element(By.ID, "button_iniciar_sesion").click()
    WebDriverWait(self.driver, 10).until(EC.url_to_be("http://localhost:3001/seleccionar"))
    assert self.driver.current_url == "http://localhost:3001/seleccionar"


  def test_registrar_usuario(self):
    global numero_aleatorio
    self.driver.get("http://localhost:3001/login")
    self.driver.set_window_size(974, 1032)
    self.driver.find_element(By.ID, "input_email").click()
    self.driver.find_element(By.ID, "input_email").send_keys("jeremyaldama23.2@gmail.com")
    self.driver.find_element(By.ID, "input_password").click()
    self.driver.find_element(By.ID, "input_password").send_keys("edumentor")
    self.driver.find_element(By.ID, "button_iniciar_sesion").click()
    WebDriverWait(self.driver, 2).until(EC.url_to_be("http://localhost:3001/seleccionar"))
    self.driver.find_element(By.ID, "Administrador").click()
    WebDriverWait(self.driver, 2).until(EC.url_to_be("http://localhost:3001/dashboard"))
    self.driver.find_element(By.ID, "Usuarios").click()
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "Registro de Usuarios")))
    WebDriverWait(self.driver, 10).until(EC.url_to_be("http://localhost:3001/dashboard/usuarios/lista"))
    self.driver.find_element(By.ID, "Registro de Usuarios").click()
    #self.driver.find_element(By.ID, "Registro de Usuarios").click()
    #WebDriverWait(self.driver, 2).until(EC.url_to_be("http://localhost:3001/dashboard/usuarios/registrar"))
    #self.driver.find_element(By.ID, "inline-radio-un-usario").click()
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "input_codigo")))
    self.driver.find_element(By.ID, "input_codigo").click()
    numero_aleatorio = random.randint(20180000, 20259999)
    numero_aleatorio_str = str(numero_aleatorio)
    self.driver.find_element(By.ID, "input_codigo").send_keys(numero_aleatorio_str)
    nombre=random.choice(nombres)
    self.driver.find_element(By.ID, "input_Nombres").send_keys(nombre)
    apellido=random.choice(apellidos)
    self.driver.find_element(By.ID, "input_apellidos").send_keys(apellido)
    self.driver.find_element(By.ID, "input_correo").send_keys(nombre.lower()+"."+apellido.lower()+"@pucp.edu.pe")
    numero_aleatorio2 = random.randint(900000000, 999999999)
    numero_aleatorio2_str = str(numero_aleatorio2)
    self.driver.find_element(By.ID, "input_telefono").send_keys(numero_aleatorio2)
    trigger = WebDriverWait(self.driver, 10).until(
      EC.element_to_be_clickable((By.ID, "select_Rol_usario"))
    )
    trigger.click()
    # Espera a que las opciones sean visibles y selecciona la primera opción
    # Asume que la clase 'SelectItem' se utiliza para los items individuales
    self.driver.find_element(By.ID, "select_Rol_Alumno").click()
    trigger = WebDriverWait(self.driver, 10).until(
      EC.element_to_be_clickable((By.ID, "select_facultad_alumno"))
    )
    trigger.click()
    # Espera a que las opciones sean visibles y selecciona la primera opción
    # Asume que la clase 'SelectItem' se utiliza para los items individuales
    primera_opcion = WebDriverWait(self.driver, 10).until(
      EC.visibility_of_element_located((By.CSS_SELECTOR, "[id^='select-item-facultad-']:first-child"))
    )
    primera_opcion.click()
    trigger = WebDriverWait(self.driver, 10).until(
      EC.element_to_be_clickable((By.ID, "select_programa_alumno"))
    )
    trigger.click()
    # Espera a que las opciones sean visibles y selecciona la primera opción
    # Asume que la clase 'SelectItem' se utiliza para los items individuales
    primera_opcion = WebDriverWait(self.driver, 10).until(
      EC.visibility_of_element_located((By.CSS_SELECTOR, "[id^='select-item-programa-']:first-child"))
    )
    primera_opcion.click()
    self.driver.find_element(By.ID, "button_registrar_usuario").click()
    primera_opcion = WebDriverWait(self.driver, 10).until(
      EC.visibility_of_element_located((By.ID, "mensaje_confirmacion"))
    )
    self.driver.find_element(By.ID, "mensaje_confirmacion").get_attribute("id")
    assert self.driver.find_element(By.ID, "mensaje_confirmacion").get_attribute("id") == "mensaje_confirmacion"

  def test_asignar_Alumno_a_Tutoria(self):
    global numero_aleatorio
    self.driver.get("http://localhost:3001/login")
    self.driver.set_window_size(974, 1032)
    self.driver.find_element(By.ID, "input_email").click()
    self.driver.find_element(By.ID, "input_email").send_keys("jeremyaldama23.2@gmail.com")
    self.driver.find_element(By.ID, "input_password").click()
    self.driver.find_element(By.ID, "input_password").send_keys("edumentor")
    self.driver.find_element(By.ID, "button_iniciar_sesion").click()
    WebDriverWait(self.driver, 10).until(EC.url_to_be("http://localhost:3001/seleccionar"))
    self.driver.find_element(By.ID, "ResponsabledeFacultad").click()
    WebDriverWait(self.driver, 10).until(EC.url_to_be("http://localhost:3001/dashboard"))
    self.driver.find_element(By.ID, "Alumnos").click()
    #time.sleep(2)
    self.driver.find_element(By.ID, "Asignación de Tutoría").click()
    self.driver.find_element(By.ID, "Asignación de Tutoría").click()
    WebDriverWait(self.driver, 10).until(EC.url_to_be("http://localhost:3001/dashboard/alumnos/asignar-tutoria"))
    # Espera a que las opciones sean visibles y selecciona la primera opción
    # Asume que la clase 'SelectItem' se utiliza para los items individuales
    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "selectGeneral")))
    self.driver.find_element(By.ID, "selectGeneral").click()
    primera_opcion = WebDriverWait(self.driver, 10).until(
      EC.visibility_of_element_located((By.CSS_SELECTOR, "[id^='selected-tutoria-']:first-child"))
    )
    primera_opcion.click()
    self.driver.find_element(By.ID, "codigoAlumno").send_keys(str(numero_aleatorio))
    self.driver.find_element(By.ID, "agregarAlumno").click()
    #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "guardarAlumnoAsignado")))
    button = WebDriverWait(self.driver, 10).until(
      EC.presence_of_element_located((By.ID, "guardarAlumnoAsignado"))
    )
    actions = ActionChains(self.driver)
    actions.move_to_element(button).perform()

    # Ahora intenta hacer clic en el botón
    button.click()
    primera_opcion = WebDriverWait(self.driver, 10).until(
      EC.visibility_of_element_located((By.CSS_SELECTOR, "[id^='mensaje_confirmacion']"))
    )
    assert primera_opcion.get_attribute("id") == "mensaje_confirmacion"

  def test_asignarTutor(self):
    global numero_aleatorio
    self.driver.get("http://localhost:3001/login")
    self.driver.set_window_size(974, 1032)
    self.driver.find_element(By.ID, "input_email").click()
    self.driver.find_element(By.ID, "input_email").send_keys("jeremyaldama23.2@gmail.com")
    self.driver.find_element(By.ID, "input_password").click()
    self.driver.find_element(By.ID, "input_password").send_keys("edumentor")
    self.driver.find_element(By.ID, "button_iniciar_sesion").click()
    WebDriverWait(self.driver, 10).until(EC.url_to_be("http://localhost:3001/seleccionar"))
    self.driver.find_element(By.ID, "ResponsabledeFacultad").click()
    WebDriverWait(self.driver, 10).until(EC.url_to_be("http://localhost:3001/dashboard"))
    self.driver.find_element(By.ID, "Asignar Tutor").click()

    WebDriverWait(self.driver, 2).until(EC.url_to_be("http://localhost:3001/dashboard/asignar-tutor"))
    # time.sleep(2)
    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "select-tutorria-trigger")))
    self.driver.find_element(By.ID, "select-tutorria-trigger").click()
    # Espera a que las opciones sean visibles y selecciona la primera opción
    # Asume que la clase 'SelectItem' se utiliza para los items individuales
    primera_opcion = WebDriverWait(self.driver, 10).until(
      EC.visibility_of_element_located((By.CSS_SELECTOR, "[id^='select-item-tutoria-']:first-child"))
    )
    primera_opcion.click()
    # time.sleep(2)
    trigger = WebDriverWait(self.driver, 10).until(
      EC.element_to_be_clickable((By.ID, "select-tutor-trigger"))
    )
    trigger.click()
    # Espera a que las opciones sean visibles y selecciona la primera opción
    # Asume que la clase 'SelectItem' se utiliza para los items individuales
    primera_opcion = WebDriverWait(self.driver, 10).until(
      EC.visibility_of_element_located((By.CSS_SELECTOR, "[id^='select-item-tutor-']:first-child"))
    )
    primera_opcion.click()
    # time.sleep(2)
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "codigo")))
    self.driver.find_element(By.ID, "codigo").click()
    self.driver.find_element(By.ID, "codigo").send_keys(str(numero_aleatorio))
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "btnAsignar")))
    self.driver.find_element(By.ID, "btnAsignar").click()
    # time.sleep(2)
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, str(numero_aleatorio))))
    self.driver.find_element(By.ID, str(numero_aleatorio)).get_attribute("id")
    assert self.driver.find_element(By.ID, str(numero_aleatorio)).get_attribute("id") == str(numero_aleatorio)
    self.driver.find_element(By.ID, "btnGuardar").click()
    primera_opcion = WebDriverWait(self.driver, 10).until(
      EC.visibility_of_element_located((By.CSS_SELECTOR, "[id^='mensaje_confirmacion']"))
    )
    assert primera_opcion.get_attribute("id") == "mensaje_confirmacion"

  def test_crearTutoria(self):
    global numero_aleatorio
    self.driver.get("http://localhost:3001/login")
    self.driver.set_window_size(974, 1032)
    self.driver.find_element(By.ID, "input_email").click()
    self.driver.find_element(By.ID, "input_email").send_keys("jeremyaldama23.2@gmail.com")
    self.driver.find_element(By.ID, "input_password").click()
    self.driver.find_element(By.ID, "input_password").send_keys("edumentor")
    self.driver.find_element(By.ID, "button_iniciar_sesion").click()
    WebDriverWait(self.driver, 10).until(EC.url_to_be("http://localhost:3001/seleccionar"))
    self.driver.find_element(By.ID, "ResponsabledeFacultad").click()
    WebDriverWait(self.driver, 10).until(EC.url_to_be("http://localhost:3001/dashboard"))
    self.driver.find_element(By.ID, "Tutorias").click()
    WebDriverWait(self.driver, 10).until(EC.url_to_be("http://localhost:3001/dashboard/tutorias"))
    self.driver.find_element(By.ID, "create_tutoria_button").click()
    WebDriverWait(self.driver, 10).until(EC.url_to_be("http://localhost:3001/dashboard/tutorias/crearTutoria"))
    self.driver.find_element(By.ID, "nombre_input").send_keys("Tutoria de Cuarta Matrícula")
    self.driver.find_element(By.ID, "descripcion_input").send_keys("Esto es una tutoria de prueba con Selenium")
    individual_radio_button = WebDriverWait(self.driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,  "//input[@type='radio'][@name='fila1']/following-sibling::label[contains(text(), 'Individual')]/preceding-sibling::input[1]")))
    individual_radio_button.click()
    individual_radio_button = WebDriverWait(self.driver, 10).until(
      EC.element_to_be_clickable((By.XPATH,
                                  "//input[@type='radio'][@name='fila2']/following-sibling::label[contains(text(), 'Obligatorio')]/preceding-sibling::input[1]")))
    individual_radio_button.click()
    individual_radio_button = WebDriverWait(self.driver, 10).until(
      EC.element_to_be_clickable((By.XPATH,
                                  "//input[@type='radio'][@name='fila3']/following-sibling::label[contains(text(), 'Permanente')]/preceding-sibling::input[1]")))
    individual_radio_button.click()
    individual_radio_button = WebDriverWait(self.driver, 10).until(
      EC.element_to_be_clickable((By.XPATH,
                                  "//input[@type='radio'][@name='fila4']/following-sibling::label[contains(text(), 'No es de Riesgo')]/preceding-sibling::input[1]")))
    individual_radio_button.click()
    individual_radio_button = WebDriverWait(self.driver, 10).until(
      EC.element_to_be_clickable((By.XPATH,
                                  "//input[@type='radio'][@name='fila5']/following-sibling::label[contains(text(), 'Tutor Variable')]/preceding-sibling::input[1]")))
    individual_radio_button.click()
    self.driver.find_element(By.ID, "guardar_tutoria").click()
    individual_radio_button = WebDriverWait(self.driver, 10).until(
      EC.element_to_be_clickable((By.ID,"confirmar_confirmacion_tutoria")))
    individual_radio_button.click()
    primera_opcion = WebDriverWait(self.driver, 10).until(
      EC.visibility_of_element_located((By.CSS_SELECTOR, "[id^='mensaje_confirmacion']"))
    )
    assert primera_opcion.get_attribute("id") == "mensaje_confirmacion"
  def test_reservarCita(self):
    self.driver.get("http://localhost:3001/login")
    self.driver.set_window_size(974, 1032)
    self.driver.find_element(By.ID, "input_email").click()
    self.driver.find_element(By.ID, "input_email").send_keys("wilson@pucp.edu.pe")
    self.driver.find_element(By.ID, "input_password").click()
    self.driver.find_element(By.ID, "input_password").send_keys("edumentor")
    self.driver.find_element(By.ID, "button_iniciar_sesion").click()
    WebDriverWait(self.driver, 10).until(EC.url_to_be("http://localhost:3001/seleccionar"))
    self.driver.find_element(By.ID, "Alumno").click()
    WebDriverWait(self.driver, 10).until(EC.url_to_be("http://localhost:3001/dashboard"))
    self.driver.find_element(By.ID, "Tutorias").click()
    WebDriverWait(self.driver, 10).until(EC.url_to_be("http://localhost:3001/dashboard/tutorias"))
    WebDriverWait(self.driver, 10).until(
      EC.element_to_be_clickable((By.ID,"button-Tutoria de prueba3"  )))
    self.driver.find_element(By.ID, "button-Tutoria de prueba3").click()
    WebDriverWait(self.driver, 10).until(EC.url_to_be("http://localhost:3001/dashboard/tutorias/detalle-tutorias/1?tutoriaId=8&alumnoId=1"))
    self.driver.find_element(By.ID, "solicitar_cita").click()
    WebDriverWait(self.driver, 10).until(EC.url_to_be("http://localhost:3001/dashboard/tutorias/solicitarCita?tutoriaId=8&idAlumno=1"))
    self.driver.find_element(By.ID, "input_motivo").click()
    self.driver.find_element(By.ID, "input_motivo").send_keys("3 laboratorios jalados")
    individual_radio_button = WebDriverWait(self.driver, 10).until(
      EC.element_to_be_clickable((By.XPATH,
                                  '//button[contains(@class, "react-calendar__navigation__next-button") and @aria-label=""]')))
    individual_radio_button.click()
    individual_radio_button = WebDriverWait(self.driver, 10).until(
      EC.element_to_be_clickable((By.XPATH,
                                  "//button[abbr[@aria-label='3 de junio de 2024']]")))
    individual_radio_button.click()
    horas_a_buscar = ['20:00',]

    # Inicializa la variable para el botón encontrado
    individual_radio_button = None

    # Intenta encontrar el botón con las horas en orden
    for hora in horas_a_buscar:
        try:
            individual_radio_button = WebDriverWait(self.driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, f'//button[text()="{hora}"]'))
            )
            # Si se encuentra el botón, sale del bucle
            break
        except TimeoutException:
            # Si no se encuentra el botón, continúa con la siguiente hora
            continue

    # Verifica si se encontró un botón
    if individual_radio_button:
        individual_radio_button.click()
        print(f'Botón con la hora {hora} fue clicado.')
        
    else:
        print('No se encontró ningún botón con las horas especificadas.')

    self.driver.find_element(By.ID, "bttn_agendarCita").click()
    try:
      # Espera hasta que el elemento h2 con el id y el texto especificado sea visible
      mensaje_exito = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(
          (By.ID, "bttn_aceptar"))
      )
      print('El mensaje de éxito ha sido encontrado:', mensaje_exito.text)
    except TimeoutException:
      print('No se encontró el mensaje de éxito en el tiempo esperado.')
  def test_ObligatoriedadPersonaContacto(self):
    global numero_aleatorio
    self.driver.get("http://localhost:3001/login")
    self.driver.set_window_size(974, 1032)
    self.driver.find_element(By.ID, "input_email").click()
    self.driver.find_element(By.ID, "input_email").send_keys("jeremyaldama23.2@gmail.com")
    self.driver.find_element(By.ID, "input_password").click()
    self.driver.find_element(By.ID, "input_password").send_keys("edumentor")
    self.driver.find_element(By.ID, "button_iniciar_sesion").click()
    WebDriverWait(self.driver, 10).until(EC.url_to_be("http://localhost:3001/seleccionar"))
    self.driver.find_element(By.ID, "Administrador").click()
    WebDriverWait(self.driver, 10).until(EC.url_to_be("http://localhost:3001/dashboard"))
    self.driver.find_element(By.ID, "Unidades").click()
    WebDriverWait(self.driver, 10).until(EC.url_to_be("http://localhost:3001/dashboard/unidades"))
    self.driver.find_element(By.ID, "nuevaUnidad").click()
    WebDriverWait(self.driver, 10).until(
      EC.element_to_be_clickable((By.ID, "Nombre_unidadInput")))
    self.driver.find_element(By.ID, "Nombre_unidadInput").click()
    self.driver.find_element(By.ID, "Nombre_unidadInput").send_keys("Unidad de Prueba Automatizada")
    self.driver.find_element(By.ID, "emailInput").click()
    self.driver.find_element(By.ID, "emailInput").send_keys("unida.prueba@pucp.edu.pe")
    self.driver.find_element(By.ID, "guardar_button").click()
    assert WebDriverWait(self.driver, 10).until(
      EC.visibility_of_element_located((By.ID, "persona_inputError")))
    time.sleep(2)
  def test_NuevaUnidad(self):
    global numero_aleatorio
    self.driver.get("http://localhost:3001/login")
    self.driver.set_window_size(974, 1032)
    self.driver.find_element(By.ID, "input_email").click()
    self.driver.find_element(By.ID, "input_email").send_keys("jeremyaldama23.2@gmail.com")
    self.driver.find_element(By.ID, "input_password").click()
    self.driver.find_element(By.ID, "input_password").send_keys("edumentor")
    self.driver.find_element(By.ID, "button_iniciar_sesion").click()
    WebDriverWait(self.driver, 10).until(EC.url_to_be("http://localhost:3001/seleccionar"))
    self.driver.find_element(By.ID, "Administrador").click()
    WebDriverWait(self.driver, 10).until(EC.url_to_be("http://localhost:3001/dashboard"))
    self.driver.find_element(By.ID, "Unidades").click()
    WebDriverWait(self.driver, 10).until(EC.url_to_be("http://localhost:3001/dashboard/unidades"))
    self.driver.find_element(By.ID, "nuevaUnidad").click()
    WebDriverWait(self.driver, 10).until(
      EC.element_to_be_clickable((By.ID, "Nombre_unidadInput")))
    self.driver.find_element(By.ID, "Nombre_unidadInput").click()
    self.driver.find_element(By.ID, "Nombre_unidadInput").send_keys("Unidad de Prueba Automatizada")
    self.driver.find_element(By.ID, "persona_input").click()
    self.driver.find_element(By.ID, "persona_input").send_keys("Robot en pruebas")
    self.driver.find_element(By.ID, "emailInput").click()
    self.driver.find_element(By.ID, "emailInput").send_keys("unida.prueba@pucp.edu.pe")
    self.driver.find_element(By.ID, "guardar_button").click()
    assert WebDriverWait(self.driver, 10).until(
      EC.visibility_of_element_located((By.ID, "mensaje_confirmacion")))
    time.sleep(2)