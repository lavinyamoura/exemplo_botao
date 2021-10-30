import wpilib 
import wpilib.drive 
import ctre 
class Myrobot(wpilib.TimedRobot):
    def robotInit(self):
        #criando motores
        self.m_puxar = ctre.WPI_VictorSPX(20)
        self.m_jogar = ctre.WPI_VictorSPX(31)
        self.m_empurrar = ctre.WPI_VictorSPX(9)
        self.m_subir = ctre.WPI_VictorSPX(18)
        self.stick = wpilib.Joystick(0)
#criando o teleoperado
    def teleopInit(self):
        self.myrobot.setSafetyEnabled(True)
#progrmando o teleoperado
    def teleopPeriodic(self):
        #botao 0 motor m_puxar
        if self.stick.getRawButton(0) == True: 
            self.m_puxar.set(1)
        else:
            self.m_puxar.set(0)
        #botao 1 motor m_jogar
        if self.stick.getRawButton(1) == True: 
            self.m_jogar.set(1)
        else:
            self.m_jogar.set(0)
        #botao 2 motor m_empurrar 
        if self.stick.getRawButton(2) == True:
            self.m_empurrar.set(1)
        else:
            self.m_empurrar.set(0)
        #botao 3 motor m_subir 
        if self.stick.getRawButton(3) == True:
            self.m_subir.set(1)
        else:
            self.m_subir.set(0)
        
  
