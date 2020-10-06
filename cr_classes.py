from abc import ABC

class CR(ABC):
    def __init__(self, cr, xp):
        self._cr = cr
        self._xp = xp
    
    @property
    def xp(self):
        return self._xp
    
    @property
    def cr(self):
        return self._cr
    
    def __repr__(self):
        return 'CR: {} XP: {}'.format(self._cr, self._xp)

class CR0(CR):
            def __init__(self):
                self._cr = 0
                self._xp = 0
                self._proficiency_bonus = 2

class CR1_8(CR):
            def __init__(self):
                self._cr = 1/8
                self._xp = 25
                self._proficiency_bonus = 2

class CR1_4(CR):
            def __init__(self):
                self._cr = 1/4
                self._xp = 50
                self._proficiency_bonus = 2

class CR1_2(CR):
            def __init__(self):
                self._cr = 1/2
                self._xp = 100
                self._proficiency_bonus = 2

class CR1(CR):
            def __init__(self):
                self._cr = 1
                self._xp = 200
                self._proficiency_bonus = 2
class CR2(CR):
            def __init__(self):
                self._cr = 2
                self._xp = 450
                self._proficiency_bonus = 2
class CR3(CR):
            def __init__(self):
                self._cr = 3
                self._xp = 700
                self._proficiency_bonus = 2
class CR4(CR):
            def __init__(self):
                self._cr = 4
                self._xp = 1100
                self._proficiency_bonus = 2
class CR5(CR):
            def __init__(self):
                self._cr = 5
                self._xp = 1800
                self._proficiency_bonus = 3
class CR6(CR):
            def __init__(self):
                self._cr = 6
                self._xp = 2300
                self._proficiency_bonus = 3
class CR7(CR):
            def __init__(self):
                self._cr = 7
                self._xp = 2900
                self._proficiency_bonus = 3
class CR8(CR):
            def __init__(self):
                self._cr = 8
                self._xp = 3900
                self._proficiency_bonus = 3
class CR9(CR):
            def __init__(self):
                self._cr = 9
                self._xp = 5000
                self._proficiency_bonus = 4
class CR10(CR):
            def __init__(self):
                self._cr = 10
                self._xp = 5900
                self._proficiency_bonus = 4
class CR11(CR):
            def __init__(self):
                self._cr = 11
                self._xp = 7200
                self._proficiency_bonus = 4
class CR12(CR):
            def __init__(self):
                self._cr = 12
                self._xp = 8400
                self._proficiency_bonus = 4
class CR13(CR):
            def __init__(self):
                self._cr = 13
                self._xp = 10000
                self._proficiency_bonus = 5
class CR14(CR):
            def __init__(self):
                self._cr = 14
                self._xp = 11500
                self._proficiency_bonus = 5
class CR15(CR):
            def __init__(self):
                self._cr = 15
                self._xp = 13000
                self._proficiency_bonus = 5
class CR16(CR):
            def __init__(self):
                self._cr = 16
                self._xp = 15000
                self._proficiency_bonus = 5
class CR17(CR):
            def __init__(self):
                self._cr = 17
                self._xp = 18000
                self._proficiency_bonus = 6
class CR18(CR):
            def __init__(self):
                self._cr = 18
                self._xp = 20000
                self._proficiency_bonus = 6
class CR19(CR):
            def __init__(self):
                self._cr = 19
                self._xp = 22000
                self._proficiency_bonus = 6
class CR20(CR):
            def __init__(self):
                self._cr = 20
                self._xp = 25000
                self._proficiency_bonus = 6
class CR21(CR):
            def __init__(self):
                self._cr = 21
                self._xp = 33000
                self._proficiency_bonus = 7
class CR22(CR):
            def __init__(self):
                self._cr = 22
                self._xp = 41000
                self._proficiency_bonus = 7
class CR23(CR):
            def __init__(self):
                self._cr = 23
                self._xp = 50000
                self._proficiency_bonus = 7
class CR24(CR):
            def __init__(self):
                self._cr = 24
                self._xp = 62000
                self._proficiency_bonus = 7
class CR25(CR):
            def __init__(self):
                self._cr = 25
                self._xp = 75000
                self._proficiency_bonus = 8
class CR26(CR):
            def __init__(self):
                self._cr = 26
                self._xp = 90000
                self._proficiency_bonus = 8
class CR27(CR):
            def __init__(self):
                self._cr = 27
                self._xp = 105000
                self._proficiency_bonus = 8
class CR28(CR):
            def __init__(self):
                self._cr = 28
                self._xp = 120000
                self._proficiency_bonus = 8
class CR29(CR):
            def __init__(self):
                self._cr = 29
                self._xp = 135000
                self._proficiency_bonus = 9
class CR30(CR):
            def __init__(self):
                self._cr = 30
                self._xp = 155000
                self._proficiency_bonus = 9
classmap = {
        '1_8': CR1_8,
        '1_4': CR1_4,
        '1_2': CR1_2,
'0': CR0,
'1': CR1,
'2': CR2,
'3': CR3,
'4': CR4,
'5': CR5,
'6': CR6,
'7': CR7,
'8': CR8,
'9': CR9,
'10': CR10,
'11': CR11,
'12': CR12,
'13': CR13,
'14': CR14,
'15': CR15,
'16': CR16,
'17': CR17,
'18': CR18,
'19': CR19,
'20': CR20,
'21': CR21,
'22': CR22,
'23': CR23,
'24': CR24,
'25': CR25,
'26': CR26,
'27': CR27,
'28': CR28,
'29': CR29,
'30': CR30,
}
