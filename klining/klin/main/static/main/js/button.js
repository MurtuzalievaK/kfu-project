
document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('.send-order');
    form.addEventListener('submit', function(e) {
        e.preventDefault(); // Предотвращаем обычную отправку формы
        var formData = new FormData(form);

        fetch('{% url "send_order" %}', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': '{{ csrf_token }}'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Показываем всплывающее окно
                document.getElementById('successModal').style.display = 'flex';
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });

    // Закрытие модального окна
    document.querySelector('.close').addEventListener('click', function() {
        document.getElementById('successModal').style.display = 'none';
    });
});

