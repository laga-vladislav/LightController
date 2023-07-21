# **LightController**
LightController – программный продукт для Windows, призванный упростить взаимодействие с устройствами умного дома. В частности, упор делается на управление светом, но по мере развития ПО планируется интеграция и устройств другого типа.
Функции:
* Управление основными возможностями устройств (например, включение, выключение, цветовая температура и т.д.)
* Создание сценариев.
Сценарии (в  Windows называются задачами) – минипрограммы, срабатывающие при определённых действиях в системе.

* **Работа с устройствами**. У пользователя должна быть возможность находить устройства в локальной сети, запоминать их, а также переименовывать, удалять, менять местами, группировать и так далее.
	* Группы. Устройства можно группировать. Возможно, сделать встроенные группы с комнатами, как во всех подобных приложениях. Но в целом, пользователь должен иметь возможность группировать устройства как ему вздумается.
* **Работа со сценариями.** Пользователь сможет создавать сценарии с разными триггерами, встроенными в систему. Например, при входе пользователя, или в определённое время. Но также должны быть и кастомные триггеры, например, наступление заката или рассвета.
  Сценарии планируются быть реализованными при помощи Python скриптов, скомпилированных в .exe файлы.

Дизайн должен быть простым и минималистичным, с приятными постельными цветами, а также поддерживать как светлую, так и тёмную темы.