import re


class Insulin:
    """ Class for Insulin representation """

    def __init__(self, name, onset, peak, duration):
        self.name = name
        self.onset = onset
        self.peak = peak
        self.duration = duration

    def get_names(self):
        """
        The function returns the name of an insulin
        """
        return self.name

    def get_onset(self):
        """
        The function returns medium onset of an insulin
        """
        lst = re.findall('\d+', self.onset)
        n = 0
        for el in lst:
            el = int(el)
            if el < 10:
                el *= 60
            n += el
        if len(lst) >= 1:
            return n / len(lst)
        else:
            return self.onset

    def get_peak(self):
        """
        The function returns medium peak of an insulin
        """
        lst = re.findall('\d+', self.peak)
        n = 0
        for el in lst:
            el = int(el)
            if el < 10:
                el *= 60
            n += el
        if len(lst) >= 1:
            return n / len(lst)
        else:
            return self.peak

    def get_duration(self):
        """
        The function returns maximal amd minimal time of duration of an insulin
        """
        lst = re.findall('\d+', self.duration)
        if len(lst) == 1:
            minimal = 0
            maximal = int(lst[0])
        elif len(lst) == 2:
            minimal = int(lst[0])
            maximal = int(lst[1])
        else:
            minimal = 1
            maximal = 2
        return minimal, maximal

    def insulin_type(self):
        """
        The function returns type of an insulin
        """
        if "/" in self.name:
            return "Pre-Mixed"
        elif isinstance(self.get_peak(), str):
            return "Rapid-acting"
        elif 0 < self.get_peak() <= 90:
            return "Rapid-acting"
        elif 90 < self.get_peak() <= 60 * 4:
            return "Short-acting"
        elif 4 * 60 < self.get_peak() <= 60 * 7:
            return "Long-acting"
        elif 7* 60 < self.get_peak() <= 60 * 9:
            return "Intermediate-acting"
        else:
            return "Special type"

    def __str__(self):
        """
        The function returns a string representation of an insulin
        """
        mini, maxi = self.get_duration()
        if self.insulin_type() == "Pre-Mixed":
            return "{} є мішаний інсулін. Цуй вид зазвичай споживається 2-3 рази на день перед прийняттям їжі. " \
                   "Для нього характерні наступні властивості. Середнє значення початку дії препарату є {}," \
                   " середнє значення піку дії препарату є {} максимальна тривалість - " \
                    "{}, мінімальна тривалість - {}.".format(self.name, self.get_onset(), self.get_peak(), maxi, mini)
        elif self.insulin_type() == "Pre-Mixed":
            return "{} є мішаний інсулін. Цуй вид зазвичай споживається 2-3 рази на день перед прийняттям їжі. " \
                   "Для нього характерні наступні властивості. Середнє значення початку дії препарату є {}," \
                   " середнє значення піку дії препарату є {} максимальна тривалість - " \
                    "{}, мінімальна тривалість - {}.".format(self.name, self.get_onset(), self.get_peak(), maxi, mini)
        elif self.insulin_type() == "Rapid-acting":
            return "{} - інсулін раптової дії. Він покриває потребу в інсуліні під-час прийому їжі . This type of " \
                   "insulin is often used with longer-acting insulin. Для нього характерні наступні властивості. " \
                   "Середнє значення початку дії препарату є {}, середнє значення піку дії препарату є {} " \
                   "максимальна тривалість - {}, мінімальна тривалість -" \
                   " {}.".format(self.name, self.get_onset(), self.get_peak(), maxi, mini)
        elif self.insulin_type() ==  "Short-acting":
            return "{} - інсулін короткої дії. Покривє потребу в інсуліні за 10 - 30 хв вісля прийому їжі" \
                   "Для нього характерні наступні властивості. Середнє значення початку дії препарату є {}," \
                   " середнє значення піку дії препарату є {} максимальна тривалість - " \
                    "{}, мінімальна тривалість - {}.".format(self.name, self.get_onset(), self.get_peak(), maxi, mini)
        elif self.insulin_type() == "Intermediate-acting":
            return "{} - інсулін середньої дії. Покриває потребу в інсуліна за половину дня. Цей вид інсуліну часто " \
                   "поєднується з інсульном короткої або раптової дії. Для нього характерні наступні властивості. " \
                   "Середнє значення початку дії препарату є {}," \
                   " середнє значення піку дії препарату є {} максимальна тривалість - " \
                    "{}, мінімальна тривалість - {}.".format(self.name, self.get_onset(), self.get_peak(), maxi, mini)
        elif self.insulin_type() == "Long-acting":
            return "{} - інсулін довгої дії що покриваж потребу в інсуліні за цілий день ей вид інсуліну часто " \
                   "поєднується з інсульном короткої або раптової дії." \
                    "Для нього характерні наступні властивості. Середнє значення початку дії препарату є {}," \
                   " середнє значення піку дії препарату є {} максимальна тривалість - " \
                    "{}, мінімальна тривалість - {}.".format(self.name, self.get_onset(), self.get_peak(), maxi, mini)
        else:
            return "{} -особливий вид інсуліну. Для нього характерні наступні властивості. Середнє значення " \
                   "початку дії препарату є {}, середнє значення піку дії препарату є {} максимальна тривалість - " \
                    "{}, мінімальна тривалість - {}.".format(self.name, self.get_onset(), self.get_peak(), maxi, mini)

