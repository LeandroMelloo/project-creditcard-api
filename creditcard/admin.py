from django.contrib import admin

from creditcard.models import CreditCard


class CreditCardAdmin(admin.ModelAdmin):
    """
    Classe de administração para o modelo CreditCard.

    Esta classe define as configurações de exibição e pesquisa para o modelo CreditCard
    no painel de administração do Django.

    Attributes:
        model (CreditCard): O modelo a ser administrado.
        list_display (tuple): Tupla contendo os campos a serem exibidos na lista de registros do modelo.
        search_fields (tuple): Tupla contendo os campos pelos quais os registros podem ser pesquisados.

    """

    model = CreditCard
    list_display = (
        "id",
        "exp_date",
        "holder",
        "number",
        "cvv",
    )
    search_fields = (
        "id",
        "exp_date",
        "holder",
        "number",
        "cvv",
    )


admin.site.register(CreditCard, CreditCardAdmin)
