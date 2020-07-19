import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime
r = sr.Recognizer()

def record_audio(ask = False):
        with sr.Microphone() as source:
            if ask:
                peBo_speak(ask)
            audio = r.listen(source)
            voice_data = ''
            try:
              voice_data = r.recognize_google(audio)
            except sr.UnknownValueError:
                peBo_speak('Sorry, I did not get that')
            except sr.RequestError:
                peBo_speak('Sorry, my speech services are down')
            return voice_data

def peBo_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    #print(audio_string)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'what is your name' in voice_data:
        peBo_speak('''My name is Pebo''')
    if 'what is friction' in voice_data:
        peBo_speak('''Friction is the resistance to motion of one object moving relative to another. 
        When surfaces in contact move relative to each other, the friction between the two surfaces 
        converts kinetic energy into thermal energy. Friction is a non fundamental and non conservative 
        force.''')
    if 'what is the coefficient of friction' in voice_data:
        peBo_speak('''A coefficient of friction is a dimensionless scalar value that shows the relationship 
        between two objects and the normal reaction between the objects that are involved.''')
    if 'name different types of friction' in voice_data:
        peBo_speak('''The limiting maximum static frictional force depends upon the nature of the surfaces
         in contact. It does not depend upon the size or area of the surfaces. For the given surfaces, the 
         limiting frictional force f s is directly proportional to the normal reaction N. F s is equal to mu
         s multiplied by N. Where the constant of proportionality mu s is called the coefficient of static 
         friction. The said formula holds only when f s has its maximum, limiting value.''')
    if 'what is angle of friction' in voice_data:
        peBo_speak('''In the case of limiting friction, the angle which the resultant R of the limiting force 
        f s and the normal reaction N makes with the normal reaction N is called the angle of friction.''')
    if 'what is force' in voice_data:
        peBo_speak('''A Force is that physical cause which changes or tends to change either the size or shape
         or the state of rest or motion of the body.''')
    if 'what are contact forces' in voice_data:
        peBo_speak('''The forces which act on bodies when they are in physical contact are called the Contact forces.''')
    if 'what are non contact forces' in voice_data:
        peBo_speak('''The forces experienced by bodies even without being physically touched are called the Non-Contact 
        Forces or the Forces at a distance.''')
    if 'what are gravitational forces' in voice_data:
        peBo_speak('''The body on a force due to the earth's attraction is called the force of Gravity. In the universe,
        all particles attract one another due to its mass.''')
    if 'what is meant by turning effect of force' in voice_data:
        peBo_speak('''The turning effect of a force acting on a body about an axis is due to the moment of force or 
        torque. It depends on the magnitude of a force applied and the distance of the line of action of force from the 
        axis of rotation.''')
    if 'what is moment of force' in voice_data:
        peBo_speak('''If a force is applied to the end of an object whose other end is attached to a pivot or hinge, 
        the force will tend to rotate the object about the pivot, called the fulcrum, Thus, a force can, in certain 
        circumstances, have a turning effect. We call this effect the Moment of the Force. It is equal to the product 
        of the magnitude of the force and the perpendicular distance of the line of action of force from the axis of 
        rotation. It is a vector quantity.''')
    if 'what is projectile motion' in voice_data:
        peBo_speak('''When any object is thrown from horizontal at an angle θ except 90°, then the path followed by it
        is called trajectory, the object is called projectile and its motion is called projectile motion.''')
    if 'what is time of flight' in voice_data:
        peBo_speak('''It is defined as the total time for which the projectile remains in air.
        T = (2 u sin θ) divided by g ''')
    if 'what is maximum height' in voice_data:
        peBo_speak('''It is defined as the maximum vertical distance covered by projectile.
        H = (u squire sin squire θ) divided by 2 g''')
    if 'what is horizontal range' in voice_data:
        peBo_speak('''It is defined as the maximum distance covered in horizontal distance.
        R = (u squire sin 2 θ) divided by g''')
    if '''what are Newton's Law of Motion''' in voice_data:
        peBo_speak('''If the net external force on a body is zero, its acceleration is zero.  Acceleration can be non 
        zero only if there is a net external force on the body.

        The rate of change of momentum of a body is directly proportional to the applied force and takes place in the 
        direction in which the force acts.

        To every action, there is always an equal and opposite reaction ''')
    if 'what do you mean by principle of conservation of energy' in voice_data:
        peBo_speak('The sum of all kinds of energies in an isolated system remains constant at all times.')
    if 'what do you mean by principle of conservation of mechanical energy' in voice_data:
        peBo_speak('''For conservative forces the sum of kinetic and potential energy of any object remains constant 
        throughout the motion. According to quantum physics, mass and energy are not conserved separately but are 
        conserved as a single entity called ‘mass-energy’.''')
    if 'collisions' in voice_data:
        peBo_speak('''Collision between two or more particles is the interaction for a short interval of time in which
        they apply relatively strong forces on each other. ''')
    if 'how many types of collisions are there define them' in voice_data:
        peBo_speak('There are two types of collisions: elastic collision and Inelastic collision')
    if 'elastic collision' in voice_data:
        peBo_speak('''The collision in which both the momentum and the kinetic energy of the system remains conserved 
        are called elastic collisions.
        In an elastic collision all the involved forces are conservative forces.
        Total energy remains conserved. ''')
    if 'inelastic collision' in voice_data:
        peBo_speak('''The collision in which only the momentum remains conserved but kinetic energy does not remain 
        conserved are called inelastic collisions. In an inelastic collision some or all the involved forces are 
        non-conservative forces. Total energy of the system remains conserved.
        If after the collision two bodies stick to each other, then the collision is said to be perfectly inelastic.''')
    if 'what is coefficient of restitution or resilience' in voice_data:
        print('''The ratio of relative velocity of separation after collision to the velocity of approach before 
                collision is called coefficient of restitution resilience (e).
                It is represented by e and it depends upon the material of the colliding bodies.
                For a perfectly elastic collision, e = 1
                For a perfectly inelastic collision, e = 0
                For all other collisions, 0 < e < 1 ''')
        peBo_speak('''The ratio of relative velocity of separation after collision to the velocity of approach before 
        collision is called coefficient of restitution resilience (e).
        It is represented by e and it depends upon the material of the colliding bodies.
        For a perfectly elastic collision, e = 1
        For a perfectly inelastic collision, e = 0
        For all other collisions, 0 < e < 1 ''')

    if 'what time is it' in voice_data:
        print(ctime)
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q='+ search
        webbrower.get().open(url)
        print('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https:google.nl/maps/place' + location + '/&amp'
        webbrowser.get().open(url)
        print('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()

time.sleep(1)
peBo_speak('How I can help you')
#print('How I can help you')
while 1:
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)
