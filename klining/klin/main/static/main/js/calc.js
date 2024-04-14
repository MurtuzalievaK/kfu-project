document.addEventListener('DOMContentLoaded', function () {
    const spaceRange = document.getElementById('space');
    const serviceType = document.getElementById('serviceType');
    const cleaningFrequency = document.getElementById('cleaningFrequency');
    const priceValue = document.getElementById('priceValue');

    function calculatePrice() {
        let basePrice = 2490; // Базовая цена
        let space = parseInt(spaceRange.value);
        let discount = cleaningFrequency.value === 'weekly' ? 0.75 : 1; // Скидка 25% за еженедельную уборку

        // Расчет цены может быть более сложным в зависимости от услуги и других параметров
        let finalPrice = basePrice * space / 25 * discount;

        priceValue.textContent = `от ${finalPrice.toFixed(0)} Р`;
    }

    // Событие для обновления цены при изменении параметров
    spaceRange.addEventListener('input', function () {
        document.getElementById('spaceValue').textContent = `${spaceRange.value} м²`;
        calculatePrice();
    });

    serviceType.addEventListener('change', calculatePrice);
    cleaningFrequency.addEventListener('change', calculatePrice);

    // Инициализация цены при загрузке страницы
    calculatePrice();
});
