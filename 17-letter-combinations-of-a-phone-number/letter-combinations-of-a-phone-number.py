class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()
        phoneGrid = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '8': 'tuv',
            '7': 'pqrs',
            '9': 'wxyz'
        }
        comp = []
        for d in digits:
            comp.append(phoneGrid[d])

        combinations = [''.join(comb) for comb in product(comp, repeat=2)]
        
        return ([''.join(combo) for combo in product(*comp)])