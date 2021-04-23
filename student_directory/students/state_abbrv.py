class StateAbbrv(object):
    state_abbrv_dict = dict(Alabama='AL', Alaska='AK', Arizona='AZ', Arkansas='AR', California='CA', Colorado='CO',
                            Connecticut='CT', DistrictofColumbia='DC', Delaware='DE', Florida='FL',
                            Georgia='GA', Hawaii='HI', Idaho='ID', Illinois='IL', Indiana='IN', Iowa='IA', Kansas='KS',
                            Kentucky='KY', Louisiana='LA', Maine='ME', Maryland='MD', Massachusetts='MA',
                            Michigan='MI', Minnesota='MN', Mississippi='MS', Missouri='MO', Montana='MT', Nebraska='NE',
                            Nevada='NV', NewHampshire='NH', NewJersey='NJ', NewMexico='NM', NewYork='NY',
                            NorthCarolina='NC', NorthDakota='ND', Ohio='OH', Oklahoma='OK', Oregon='OR',
                            Pennsylvania='PA', PuertoRico='PR', RhodeIsland='RI', SouthCarolina='SC', SouthDakota='SD',
                            Tennessee='TN', Texas='TX', Utah='UT', Vermont='VT', Virginia='VA', Washington='WA',
                            WestVirginia='WV', Wisconsin='WI', Wyoming='WY')

    @staticmethod
    def generate_state_choices() -> list:
        """

        :return: list(tuples)
        """
        temp_list = list()
        temp_list.append((None, "--"))
        for state_abbv in StateAbbrv.state_abbrv_dict.values():
            temp_list.append((state_abbv, state_abbv))

        return temp_list
