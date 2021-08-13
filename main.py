from kivy.app import App
import os, sys
from kivy.resources import resource_add_path, resource_find
from kivy.properties import BooleanProperty
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager


class HomeScreen(Screen):
    pass


class Test1Intro(Screen):
    pass


class Test1Q1(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You must already hold a G class licence.'
        self.button_disabled = True


class Test1Q2(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! It should be placed on the right of the windshield or right-hand side of the bus. '
        self.button_disabled = True


class Test1Q3(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! It will be painted chrome yellow. '
        self.button_disabled = True


class Test1Q4(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You must be at least 18 years old.'
        self.button_disabled = True


class Test1Q5(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Best time would be on the way to collect your first passengers of the day. '
        self.button_disabled = True


class Test1Q6(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should always check the condition of your brakes on low speed.'
        self.button_disabled = True


class Test1Q7(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You need a C class licence.'
        self.button_disabled = True


class Test1Q8(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! They carry six or more children and/or adults with a developmental disability.'
        self.button_disabled = True


class Test1Q9(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You must be at least 21 years old.'
        self.button_disabled = True


class Test1Q10(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You must wear them at all times.'
        self.button_disabled = True


class Test1Q11(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! A bus is defined as carrying 10 or more passengers.'
        self.button_disabled = True


class Test1Q12(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! A schedule 4 inspection is valid for 30 days.'
        self.button_disabled = True


class Test1Q13(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You must submit the report every two years.'
        self.button_disabled = True


class Test1Q14(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You need an F class licence.'
        self.button_disabled = True


class Test1Q15(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! In Ontario, a bus is defined as carrying more than 10 passengers.'
        self.button_disabled = True


class Test1Q16(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Drivers must submit a yearly medical report once they reach 65 years old.'
        self.button_disabled = True


class Test1Q17(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The most common cause is driving with the parking brake on.'
        self.button_disabled = True


class Test1Q18(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! With class E licence, you may not drive a school bus with more than 24 capacity.'
        self.button_disabled = True


class Test1Q19(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You must not drive it.'
        self.button_disabled = True


class Test1Q20(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The inspection report must be completed within the last 24.'
        self.button_disabled = True


class Test1Q21(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The pressure should be the same as the highest pressure tire on your vehicle. '
        self.button_disabled = True


class Test1Q22(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You would need a class B licence.'
        self.button_disabled = True


class Test1Q23(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The certificate is valid for five years.'
        self.button_disabled = True


class Test1Q24(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You must pass all of these tests.'
        self.button_disabled = True


class Test1Q25(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You may not have more than six demerit points when driving a school bus.'
        self.button_disabled = True


class Test1Q26(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! To check, you should put the vehicle in gear while the parking brake is on.'
        self.button_disabled = True


class Test1Q27(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You need a Z endorsement on your Ontario licence.'
        self.button_disabled = True


class Test1Q28(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Driving on high speed highways is not part of the test for class C or F.'
        self.button_disabled = True


class Test1Q29(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should note it on the inspection report and report it to the operator.'
        self.button_disabled = True


class Test1Q30(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Operators are responsible for the inspection.'
        self.button_disabled = True


class Test1Fin(Screen):
    pass


class Test2Intro(Screen):
    pass


class Test2Q1(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should stop as soon as possible.'
        self.button_disabled = True


class Test2Q2(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should release the brakes then reapply. '
        self.button_disabled = True


class Test2Q3(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should choose the same gear you would use going up it.'
        self.button_disabled = True


class Test2Q4(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! A bus driver should wear a seatbelt at all times.'
        self.button_disabled = True


class Test2Q5(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! A good bus driver always shows other road users courtesy.'
        self.button_disabled = True


class Test2Q6(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should not drive a bus under any of these circumstances.'
        self.button_disabled = True


class Test2Q7(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should be ready to give it up if it will avoid possible danger.'
        self.button_disabled = True


class Test2Q8(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You may not drive a school bus for any criminal offence within the last 12 months.'
        self.button_disabled = True


class Test2Q9(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should pump the brake pedal several times.'
        self.button_disabled = True


class Test2Q10(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The pedal should drop slightly.'
        self.button_disabled = True


class Test2Q11(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! A good bus driver drives defensively.'
        self.button_disabled = True


class Test2Q12(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! All of these lights are part of the daily inspection.'
        self.button_disabled = True


class Test2Q13(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The licence may be suspended if you accumulate more than eight demerit points.'
        self.button_disabled = True


class Test2Q14(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Your front wheels should be close the the right edge of the pavement.'
        self.button_disabled = True


class Test2Q15(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The rear wheels will follow a path closer to the curb than the front wheels.'
        self.button_disabled = True


class Test2Q16(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should use all of your mirrors. '
        self.button_disabled = True


class Test2Q17(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You will have to demonstrate all of these things.'
        self.button_disabled = True


class Test2Q18(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Your front wheels should be close to the center line.'
        self.button_disabled = True


class Test2Q19(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! It depends on the distance between front and rear wheels. '
        self.button_disabled = True


class Test2Q20(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should check the brakes before joining the highway. '
        self.button_disabled = True


class Test2Q21(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should always drive at the appropriate speed for the road and weather.'
        self.button_disabled = True


class Test2Q22(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should disembark and check all around the vehicle. '
        self.button_disabled = True


class Test2Q23(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! It is best to use more space on the road you are entering.'
        self.button_disabled = True


class Test2Q24(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should not send text messages while driving a bus under any circumstances.'
        self.button_disabled = True


class Test2Q25(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should maintain a space cushion all around the bus while driving. '
        self.button_disabled = True


class Test2Q26(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should use engine compression to slow down.'
        self.button_disabled = True


class Test2Q27(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! They should not be fanned except on slippery pavement.'
        self.button_disabled = True


class Test2Q28(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The most important concern for a bus driver should be passenger safety.'
        self.button_disabled = True


class Test2Q29(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should monitor your rear wheels using your left outside mirror.'
        self.button_disabled = True


class Test2Q30(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You cannot obtain the licence if you were found guilty within the last five years.'
        self.button_disabled = True


class Test2Fin(Screen):
    pass


class Test3Intro(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class Test3Q1(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Cyclists are permitted to use any part of a lane. '
        self.button_disabled = True


class Test3Q2(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should slow down and proceed with caution.'
        self.button_disabled = True


class Test3Q3(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! They have a right to use the whole of a lane. '
        self.button_disabled = True


class Test3Q4(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should flash your left turn signals and pull out with caution.'
        self.button_disabled = True


class Test3Q5(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The first thing you should do is get everyone out and away from the vehicle.'
        self.button_disabled = True


class Test3Q6(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! First vehicle to come to a complete stop has right-of-way.'
        self.button_disabled = True


class Test3Q7(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should look and steer in the direction you want to go.'
        self.button_disabled = True


class Test3Q8(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The maximum number of hours allowed is 13.'
        self.button_disabled = True


class Test3Q9(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The minimum distance you should maintain is 60 m.'
        self.button_disabled = True


class Test3Q10(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should be especially cautious at twilight when watching for children on road.'
        self.button_disabled = True


class Test3Q11(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! They are marked with red and white X signs.'
        self.button_disabled = True


class Test3Q12(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You may not pull away until all pedestrians have safely reached the opposite ' \
                       'sidewalk. '
        self.button_disabled = True


class Test3Q13(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should stop 5 meters from the nearest rail.'
        self.button_disabled = True


class Test3Q14(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Municipal buses operated as part of the public transport service are exempt from ' \
                       'hours of service regulation. '
        self.button_disabled = True


class Test3Q15(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! All of them count as on duty hours for a bus driver.'
        self.button_disabled = True


class Test3Q16(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should slow down and let them through.'
        self.button_disabled = True


class Test3Q17(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! They increase engine noise.'
        self.button_disabled = True


class Test3Q18(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You must yield to both vehicle and pedestrians. '
        self.button_disabled = True


class Test3Q19(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! A bus driver must have 10 off-duty hours per day.'
        self.button_disabled = True


class Test3Q20(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You must have at least 8 off duty hours prior to driving a bus for 13 hours.'
        self.button_disabled = True


class Test3Q21(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This will result in a fine of up to $500.'
        self.button_disabled = True


class Test3Q22(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should turn brake retarders off.'
        self.button_disabled = True


class Test3Q23(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! School buses must stop at railway crossings under all circumstances.'
        self.button_disabled = True


class Test3Q24(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You would need 100% more sopping distance than them.'
        self.button_disabled = True


class Test3Q25(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Vehicle coming from the right have the right-of-way.'
        self.button_disabled = True


class Test3Q26(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! In this case, they are allowed to drive 12 hours that day.'
        self.button_disabled = True


class Test3Q27(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You must yield to pedestrians on the sidewalk and vehicles on the road.'
        self.button_disabled = True


class Test3Q28(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should give them a distance gap of at least 1 meter.'
        self.button_disabled = True


class Test3Q29(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! It can take up to 2 km for a train to stop even under full emergency braking.'
        self.button_disabled = True


class Test3Q30(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The driver is regarded as being on duty except when taking a lunch break.'
        self.button_disabled = True


class Test3Fin(Screen):
    pass


class Test4Intro(Screen):
    pass


class Test4Q1(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You must turn low beam headlights within 150 m of an oncoming vehicle at night. '
        self.button_disabled = True


class Test4Q2(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The greatest number of on-duty hours in a 14 day cycle is 120.'
        self.button_disabled = True


class Test4Q3(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! There is no limit. '
        self.button_disabled = True


class Test4Q4(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should use low beam headlights.'
        self.button_disabled = True


class Test4Q5(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! It is compulsory to have 72 consecutive hours off duty.'
        self.button_disabled = True


class Test4Q6(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should increase your following speed.'
        self.button_disabled = True


class Test4Q7(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The best place would be on a private road.'
        self.button_disabled = True


class Test4Q8(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should test them from a speed of 50 km/h.'
        self.button_disabled = True


class Test4Q9(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should stay on the bus with your passengers until help arrives.'
        self.button_disabled = True


class Test4Q10(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The only element not compulsory is the number on your licence.'
        self.button_disabled = True


class Test4Q11(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! It is compulsory that you have 36 consecutive hours off duty in this case.'
        self.button_disabled = True


class Test4Q12(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Most skids are a result of driving to fast for conditions. '
        self.button_disabled = True


class Test4Q13(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should use low beam headlights within 60 m behind another vehicle.'
        self.button_disabled = True


class Test4Q14(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should look up and to the right. '
        self.button_disabled = True


class Test4Q15(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should be especially cautious if the road ahead looks black and shiny.'
        self.button_disabled = True


class Test4Q16(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! It is not permissible under any circumstances.'
        self.button_disabled = True


class Test4Q17(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should avoid driving through puddles for all these reasons.'
        self.button_disabled = True


class Test4Q18(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Pavement is most slippery just after the storm starts. '
        self.button_disabled = True


class Test4Q19(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Overpasses will freeze first.'
        self.button_disabled = True


class Test4Q20(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! It may be easier if you start with the gear lever in 2nd.'
        self.button_disabled = True


class Test4Q21(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You can expect the stopping distance to be shortened by 0%.'
        self.button_disabled = True


class Test4Q22(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You do not need to keep the daily log if you do not drive further away than 160 km.'
        self.button_disabled = True


class Test4Q23(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The off-duty hours must be from some point in the preceding 14 days.'
        self.button_disabled = True


class Test4Q24(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! In this case, you have to have 24 consecutive off-duty hours.'
        self.button_disabled = True


class Test4Q25(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should hold the vehicle with the handbrake.'
        self.button_disabled = True


class Test4Q26(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should slow down.'
        self.button_disabled = True


class Test4Q27(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should do all these things.'
        self.button_disabled = True


class Test4Q28(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should pull off the road and wait for conditions to improve.'
        self.button_disabled = True


class Test4Q29(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The most on-duty hours a bus driver can undertake in this period is 70.'
        self.button_disabled = True


class Test4Q30(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should avoid all of these things.'
        self.button_disabled = True


class Test4Fin(Screen):
    pass


class Test5Intro(Screen):
    pass


class Test5Q1(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! It can extend as far as 3 m across the road.'
        self.button_disabled = True


class Test5Q2(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The vehicle may be up to 40 m in length. '
        self.button_disabled = True


class Test5Q3(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! It must be visible 150 m in both directions. '
        self.button_disabled = True


class Test5Q4(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! They are all equally dangerous on the road.'
        self.button_disabled = True


class Test5Q5(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! These signs are orange with black lettering. '
        self.button_disabled = True


class Test5Q6(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! They should be placed 30 m from the front and rear of your vehicle.'
        self.button_disabled = True


class Test5Q7(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates that you may or must do the activity indicated.'
        self.button_disabled = True


class Test5Q8(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Stopping to sleep will return you to full competence.'
        self.button_disabled = True


class Test5Q9(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should pull over for all of them.'
        self.button_disabled = True


class Test5Q10(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You must report collisions with damage exceeding $2000.'
        self.button_disabled = True


class Test5Q11(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You can be fined up to $2000.'
        self.button_disabled = True


class Test5Q12(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Snowplows carry flashing blue lights as a warning.'
        self.button_disabled = True


class Test5Q13(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should stop if you can do so safely.'
        self.button_disabled = True


class Test5Q14(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You may face a fine of up to $1000.'
        self.button_disabled = True


class Test5Q15(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! These signs are yellow/green.'
        self.button_disabled = True


class Test5Q16(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! It will be travelling at 40 km/h or less.'
        self.button_disabled = True


class Test5Q17(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This can result in jail time of up to six months.'
        self.button_disabled = True


class Test5Q18(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Bus driver in Ontario have the exemption from the ban until the beginning of 2021.'
        self.button_disabled = True


class Test5Q19(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! These collisions involving drowsiness are most likely in the early morning and ' \
                       'late afternoon. '
        self.button_disabled = True


class Test5Q20(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should move the vehicles as far off the road as possible.'
        self.button_disabled = True


class Test5Q21(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign is giving you information. '
        self.button_disabled = True


class Test5Q22(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should stay with the vehicle and ask a responsible person to find help.'
        self.button_disabled = True


class Test5Q23(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Your fine would be doubled.'
        self.button_disabled = True


class Test5Q24(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! In this case, it is illegal to follow them within 150 m.'
        self.button_disabled = True


class Test5Q25(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You are still legally obliged to exchange details.'
        self.button_disabled = True


class Test5Q26(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Warning signs have a yellow background with black letters.'
        self.button_disabled = True


class Test5Q27(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! A bus may use this lane at any time.'
        self.button_disabled = True


class Test5Q28(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Stop signs in Ontario are octagonal in shape.'
        self.button_disabled = True


class Test5Q29(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The first thing you should do is call for help.'
        self.button_disabled = True


class Test5Q30(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should slow down, pull to the right and stop.'
        self.button_disabled = True


class Test5Fin(Screen):
    pass


class Test6Intro(Screen):
    pass


class Test6Q1(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You must not change gear while crossing railway tracks.'
        self.button_disabled = True


class Test6Q2(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You must inform them within six days. '
        self.button_disabled = True


class Test6Q3(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The driver is responsible for keeping a school bus clean.'
        self.button_disabled = True


class Test6Q4(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! They should cross at a distance of 3 m from the front of the bus.'
        self.button_disabled = True


class Test6Q5(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! A vehicle requires regular inspections if carrying at least six children or adults ' \
                       'with a developmental disability. '
        self.button_disabled = True


class Test6Q6(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You must open the door to listen for approaching trains.'
        self.button_disabled = True


class Test6Q7(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should report this to the police.'
        self.button_disabled = True


class Test6Q8(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Unless the road is divided by a median, motorists must stop before reaching the bus.'
        self.button_disabled = True


class Test6Q9(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The doors should be closed but not locked.'
        self.button_disabled = True


class Test6Q10(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! It means drive with caution in approaching and moving through the intersection.'
        self.button_disabled = True


class Test6Q11(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The licence will be suspended for a minimum of five years.'
        self.button_disabled = True


class Test6Q12(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! They must stop 5 m from the nearest rail.'
        self.button_disabled = True


class Test6Q13(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You may turn right on a red light provided you stop and wait for the way to clear.'
        self.button_disabled = True


class Test6Q14(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Class B and E licence holders may only accumulate eight points.'
        self.button_disabled = True


class Test6Q15(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You must not move forward until it changed to green and the intersection is clear.'
        self.button_disabled = True


class Test6Q16(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Passengers should be seated at all times. '
        self.button_disabled = True


class Test6Q17(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! They should be practiced once a month.'
        self.button_disabled = True


class Test6Q18(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should turn the signal lights before you stop.'
        self.button_disabled = True


class Test6Q19(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This law applies to only chrome yellow school buses. '
        self.button_disabled = True


class Test6Q20(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! It will be suspended for 30 days. '
        self.button_disabled = True


class Test6Q21(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! They must stop 20 m behind your school bus.'
        self.button_disabled = True


class Test6Q22(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Only if you are at least 60 m away from any intersection may you use these lights ' \
                       'or stop arm. '
        self.button_disabled = True


class Test6Q23(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! First time driving offenders will receive a suspension of at least one year.'
        self.button_disabled = True


class Test6Q24(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! It means you must come to a stop and move through the intersection when safe.'
        self.button_disabled = True


class Test6Q25(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The responsibility is with the driver. '
        self.button_disabled = True


class Test6Q26(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should yield to vehicles from your right.'
        self.button_disabled = True


class Test6Q27(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You are responsible for making sure you have a valid licence.'
        self.button_disabled = True


class Test6Q28(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You will receive five demerit points for this.'
        self.button_disabled = True


class Test6Q29(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The signal is a white vertical bar on a dark background.'
        self.button_disabled = True


class Test6Q30(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should have a clear view of at least 150 m in each direction.'
        self.button_disabled = True


class Test6Fin(Screen):
    pass


class F1App(App):
    pass


if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    F1App().run()
