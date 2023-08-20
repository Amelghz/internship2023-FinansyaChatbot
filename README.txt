Étape 1 : Créer un Endpoint dans Laravel
Dans Laravel, vous devez créer un endpoint qui servira d'interface pour votre application Flask. Ajoutez une route et une méthode de contrôleur correspondante.

Ouvrez le fichier routes/api.php dans votre projet Laravel.
Ajoutez une nouvelle route pour l'endpoint API, par exemple :

php code:
Route::post('/get', 'FlaskChatController@getFlaskResponse');


Créez un nouveau contrôleur (si vous n'en avez pas déjà un) ou utilisez un contrôleur existant. Par exemple, créez FlaskChatController.php dans le dossier app/Http/Controllers et ajoutez la méthode getFlaskResponse :

php code:

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;

class FlaskChatController extends Controller
{
    public function getFlaskResponse(Request $request)
    {
        $msg = $request->input('msg');
        // Effectuez un appel d'API à votre application Flask
        $response = Http::post('URL_DE_VOTRE_APP_FLASK', ['msg' => $msg]);
        return response()->json(['response' => $response->json()], 200);
    }
}

Étape 2 : Intégrer les Appels d'API dans votre Site Web Laravel
Maintenant, vous pouvez intégrer les appels d'API dans vos fichiers HTML et JavaScript existants du site web Laravel pour communiquer avec votre application Flask.

Ouvrez le fichier HTML où vous souhaitez intégrer l'application Flask.
Utilisez JavaScript pour capturer les données du formulaire (message) et effectuer l'appel d'API :

code html:
<!-- Insérez ce code dans votre fichier HTML Laravel -->
<script>
    $(document).ready(function() {
        $("#messageArea").on("submit", function(event) {
            event.preventDefault();
            const rawText = $("#text").val();

            $.ajax({
                type: "POST",
                url: "/api/flask-chat",
                data: {
                    msg: rawText
                },
                success: function(data) {
                    // Utilisez 'data.response' pour récupérer la réponse de votre application Flask
                    const flaskResponse = data.response;
                    // Faites quelque chose avec la réponse de Flask, par exemple, l'afficher dans le chat
                    // ...
                },
                error: function() {
                    // Gérez les erreurs si nécessaire
                }
            });
        });
    });
</script>
